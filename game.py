import pygame
import random


class Game:
    def __init__(self, game_id):
        self.id = game_id
        self.players_connected = 0
        self.players_ready = 0
        self.players = []
        self.turn = 0
        self.timer_on = False
        self.timer = 60
        self.discord_server = ""

        self.index_deck1 = [i for i in range(10)]
        self.index_deck2 = [i for i in range(10)]
        self.index_deck3 = [i for i in range(10)]
        random.shuffle(self.index_deck1)
        random.shuffle(self.index_deck2)
        random.shuffle(self.index_deck3)

    def switch_timer(self):
        self.timer_on = not self.timer_on

    def add_player(self, p):
        aux = self.players
        if p not in aux:
            aux.append(p)
        self.players = aux

    def get_players(self):
        return self.players

    def connected(self):
        if self.players_connected == 4:
            return True
        else:
            return False

    def ready(self):
        self.players_ready = self.players_ready + 1

    def next_turn(self):
        self.turn = (self.turn + 1) % 4

    def active_player(self):
        if self.turn == 0:
            return 0
        elif self.turn == 1:
            return 2
        elif self.turn == 2:
            return 1
        elif self.turn == 3:
            return 3

    def winner(self):
        winner = -1
        for p in self.players:
            if p.pawn.index == 21:
                if p.id == 0 or p.id == 1:
                    winner = 0
                    break
                else:
                    winner = 1
                    break
        return winner

    def play(self, guessed, team, nr_squares):
        if guessed:
            for p in self.players:
                if p.team == team:
                    p.pawn.move(nr_squares)
        self.next_turn()

    def turn_back(self, team):
        for p in self.players:
            if p.team == team:
                p.pawn.takeback()

    def reset(self):
        self.turn = 0
        self.timer = 60
        for p in self.players:
            p.pawn.reset()
