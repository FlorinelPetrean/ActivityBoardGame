import pygame



class Pawn:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def move(self, x, y):
        self.x = x
        self.y = y


class Avatar:
    def __init__(self, player_id, img):
        if player_id == 0:
            self.x = 610
            self.y = 40
        elif player_id == 1:
            self.x = 810
            self.y = 40
        elif player_id == 2:
            self.x = 610
            self.y = 30 + 150 + 10
        elif player_id == 3:
            self.x = 810
            self.y = 30 + 150 + 10
        self.img = img



class Player:
    def __init__(self, player_id, name, pawn_img_string, avatar_img_string):
        self.id = player_id
        self.pawn = Pawn(100, 100, pawn_img_string)
        self.name = name
        self.avatar = Avatar(player_id, avatar_img_string)
        if player_id == 0 or player_id == 1:
            self.team = 0
        else:
            self.team = 1
