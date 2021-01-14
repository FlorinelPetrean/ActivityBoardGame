import pygame



class Pawn:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class Avatar:
    def __init__(self, id, img):
        if id == 0:
            self.x = 600
            self.y = 100
        elif id == 1:
            self.x = 700
            self.y = 100
        elif id == 2:
            self.x = 600
            self.y = 300
        elif id == 3:
            self.x = 700
            self.y = 300
        self.img = img

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class Player:
    def __init__(self, id, name, pawnImg, avatarImg):
        self.id = id
        self.pawn = Pawn(100, 100, pawnImg)
        self.name = name
        self.avatar = Avatar(id, avatarImg)
        if id == 0 or id == 1:
            self.team = 0
        else:
            self.team = 1

    def draw(self, win):
        self.avatar.draw(win)
        self.pawn.draw(win)