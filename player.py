import pygame
from constants import player0_trail, player1_trail, player2_trail, plauer3_trail

player0_trail1 = [(412, 340),
(337, 341),
(260, 341),
(186, 339),
(109, 341),
(336, 293),
(261, 295),
(185, 295),
(108, 294),
(336, 249),
(259, 249),
(185, 249),
(108, 248),
(335, 202),
(261, 202),
(184, 202),
(109, 203),
(335, 155),
(261, 158),
(184, 155),
(109, 156),
(30, 153)]

class Pawn:
    def __init__(self, player_id, img):
        self.index = 0
        self.x = 0
        self.y = 0
        if player_id == 0:
            (self.x, self.y) = player0_trail[self.index]
        if player_id == 1:
            (self.x, self.y) = player0_trail[self.index]
        if player_id == 2:
            (self.x, self.y) = player0_trail[self.index]
        if player_id == 3:
            (self.x, self.y) = player0_trail[self.index]
        self.img = img

    def get_pos(self):
        return self.x, self.y

    def move(self, x, y):
        self.index = self.index + 1
        (self.x, self.y) = player0_trail[self.index]

    def takeback(self):
        if self.index != 0:
            self.index = self.index - 1
        (self.x, self.y) = player0_trail[self.index]


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
