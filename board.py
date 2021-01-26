import pygame

class Board:
    def __init__(self, bg, deck):
        self.background = bg
        self.trail = []
        self.deck = deck

    def draw(self, screen):
        screen.blit(self.background, (0, 0))








