import pygame

class GameInstance:
    def __init__(self, bg, players, deck, teams):
        self.bg = bg
        self.players = players
        self.deck = deck
        self.teams = teams
        self.turn = 0

    def nextTurn(self):
        self.turn = (self.turn + 1) % 2


