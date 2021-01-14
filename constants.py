import pygame

bg = pygame.image.load("images/750x750bb.jpeg")
bg = pygame.transform.scale(bg, (500, 650))

pawn1 = pygame.image.load("images/001-satellite dish.png")
pawn1 = pygame.transform.scale(pawn1, (50, 50))
avatar1 = pygame.image.load("images/001-satellite dish.png")
avatar1 = pygame.transform.scale(avatar1, (80, 80))

WIDTH = 1024
HEIGHT = 650