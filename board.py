import pygame

class Board:
    def __init__(self, bg, trail, deck):
        self.background = bg
        self.trail = trail
        self.deck = deck
        self.time = 0


    def draw_buttons(self, screen):
        pass

    def draw_mesage(self, message):
        pass


    def update_time(self):
        self.time = (self.time + 1) % 61

    def draw_time(self, screen):
        pass


