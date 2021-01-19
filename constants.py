import pygame

bg = pygame.image.load("images/Activity_Board.jpeg")
bg = pygame.transform.scale(bg, (500, 650))

pawn1 = pygame.image.load("images/001-satellite dish.png")
pawn1 = pygame.transform.scale(pawn1, (50, 50))
avatar1 = pygame.image.load("images/001-satellite dish.png")
avatar1 = pygame.transform.scale(avatar1, (80, 80))


player0_trail = [(412, 340),
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

player1_trail = []
player2_trail = []
plauer3_trail = []

WIDTH = 1024
HEIGHT = 650