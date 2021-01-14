import socket
import string
from _thread import *
import pickle
from game import Game
from player import Player

server = "192.168.0.106"
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

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048 * 3))

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data.reset is True:
                        game.reset()
                    elif data.player is not None:
                        game.add_player(data.player)
                    elif data.get is False and data.player is None:
                        game.play(p, data)
                    elif data.get is True:
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
        print ("error here 1")
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
