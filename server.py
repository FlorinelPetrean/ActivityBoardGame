import json
import socket
from _thread import *
import pickle
from game import Game
from player import Player
from network import Network

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

server = IP_address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0
HEADERSIZE = 10


def send_data(clientsocket, data):
    data_to_send = pickle.dumps(data)
    data_size = bytes(f'{len(data_to_send):<{10}}', "utf-8")
    try:
        clientsocket.send(data_size + data_to_send)

    except socket.error as e:
        print(e)


def receive_data(sock):
    global msglen
    full_msg = b''
    new_msg = True
    while True:
        msg = sock.recv(16)
        if new_msg:
            # msglen = int(msg[:HEADERSIZE])
            # new_msg = False
            try:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False
            except ValueError:
                msglen = 0
                new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            data = pickle.loads(full_msg[HEADERSIZE:])
            break

    return data


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = receive_data(conn)
            data_args = data.split("|")
            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data_args[0] == "addp":
                        game.add_player(Player(p, data_args[1], data_args[2], data_args[3]))

                    elif data_args[0] == "play":
                        if data_args[1] == "yes":
                            game.play(True, int(data_args[2]), int(data_args[3]))
                        else:
                            game.play(False, int(data_args[2]), int(data_args[3]))
                        game.timer_on = False

                    elif data_args[0] == "takeback":
                        wants = [False, False, False, False]
                        for player in game.get_players():
                            if player.id == int(data_args[1]):
                                player.wants_takeback = True
                            if player.wants_takeback:
                                wants[player.id] = True
                        if wants[0] == True and wants[1] == True:
                            game.turn_back(0)
                        elif wants[2] == True and wants[3] == True:
                            game.turn_back(1)

                    elif data_args[0] == "scribble":
                        if data_args[1] == "stop":
                            game.drawn_lines.append(game.scribble_pixels)
                            game.scribble_pixels = []
                        elif data_args[1] == "reset":
                            game.scribble_pixels = []
                            game.drawn_lines = []
                        else:
                            pos = (int(data_args[1]), int(data_args[2]))
                            game.add_pixel(pos)

                    elif data_args[0] == "ready":
                        game.timer_on = True

                    elif data_args[0] == "reset":
                        game.reset()

                    send_data(conn, game)


            else:
                break
        except:
            print("error here")
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        print("error here 1")
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 4
    if idCount % 4 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
        games[gameId].players_connected = 1
    elif idCount % 4 == 2:
        p = 1
        games[gameId].players_connected = 2
    elif idCount % 4 == 3:
        p = 2
        games[gameId].players_connected = 3
    else:
        p = 3
        games[gameId].players_connected = 4

    start_new_thread(threaded_client, (conn, p, gameId))
