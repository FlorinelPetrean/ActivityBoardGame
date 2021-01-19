import json
import socket
from _thread import *
import pickle
from game import Game
from player import Player

server = "192.168.1.127"
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


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    player_data = conn.recv(2048 * 2).decode()
    [username, pawn_img, avatar_img] = player_data.split("|")
    print("Received" + username + pawn_img + avatar_img)
    if gameId in games:
        games[gameId].add_player(Player(p, username, pawn_img, avatar_img))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data == "play":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))


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
