import pygame
from constants import player0_trail, player1_trail, player2_trail, player3_trail


class Pawn:
    def __init__(self, player_id, img):
        self.index = 0
        self.trail = player0_trail
        if player_id == 1:
            self.trail = player1_trail
        if player_id == 2:
            self.trail = player2_trail
        if player_id == 3:
            self.trail = player3_trail
        (self.x, self.y) = self.trail[self.index]

        self.img = img

    def get_pos(self):
        return self.x, self.y

    def move(self, nr):
        self.index = self.index + nr
        (self.x, self.y) = self.trail[self.index]

    def takeback(self):
        if self.index != 0:
            self.index = self.index - 1
        (self.x, self.y) = self.trail[self.index]

    def reset(self):
        self.index = 0
        (self.x, self.y) = self.trail[self.index]


class Avatar:
    def __init__(self, player_id, img):
        if player_id == 0:
            self.x = 610 + 50
            self.y = 40
        elif player_id == 1:
            self.x = 810 + 50
            self.y = 40
        elif player_id == 2:
            self.x = 610 + 50
            self.y = 30 + 150 + 10
        elif player_id == 3:
            self.x = 810 + 50
            self.y = 30 + 150 + 10
        self.img = img

    def get_pos(self):
        return self.x, self.y


class Player:
    def __init__(self, player_id, name, pawn_img_string, avatar_img_string):
        self.id = player_id
        self.pawn = Pawn(player_id, pawn_img_string)
        self.name = name
        self.avatar = Avatar(player_id, avatar_img_string)
        if player_id == 0 or player_id == 1:
            self.team = 0
        else:
            self.team = 1
        self.wants_takeback = False
