import pygame

bg = pygame.image.load("images/Activity_Board.jpeg")
bg = pygame.transform.scale(bg, (500, 650))

pawn1 = pygame.image.load("images/pawn/001-satellite dish.png")
pawn1 = pygame.transform.scale(pawn1, (50, 50))
avatar1 = pygame.image.load("images/pawn/001-satellite dish.png")
avatar1 = pygame.transform.scale(avatar1, (80, 80))


avatars_pos = [(650, 20), (850, 20), (650, 20 + 150), (850, 20 + 150)]
username_pos = [(650 + 20, 125), (850 + 20, 125), (650 + 20, 25 + 250), (850 + 20, 25 + 250)]

deck1 = []
deck2 = []
deck3 = []
decks_pos = [(343, 429), (219, 425), (78, 427)]

topdeck_pos = [(319, 391), (185, 387),(52, 399)]

for i in range(10):
    location1 = "images/cards/1-deck/"
    location2 = "images/cards/2-deck/"
    location3 = "images/cards/3-deck/"
    card1 = pygame.image.load(location1 + str(i + 1) + ".jpeg")
    card2 = pygame.image.load(location2 + str(i + 1) + ".jpeg")
    card3 = pygame.image.load(location3 + str(i + 1) + ".jpeg")
    card1 = pygame.transform.scale(card1, (100 + 50, 150 + 75))
    card2 = pygame.transform.scale(card2, (100 + 50, 150 + 75))
    card3 = pygame.transform.scale(card3, (100 + 50, 150 + 75))
    deck1.append(card1)
    deck2.append(card2)
    deck3.append(card3)

player0_trail = []
player1_trail = []
player2_trail = []
player3_trail = []

coords = [(412, 340),
          (337, 341),
          (260, 341),
          (186, 339),
          (109, 341),
          #
          (108, 294),
          (185, 295),
          (261, 295),
          (336, 293),

          #
          (336, 249),
          (259, 249),
          (185, 249),
          (108, 248),
          #
          (109, 203),
          (184, 202),
          (261, 202),
          (335, 202),

          #
          (335, 155),
          (261, 158),
          (184, 155),
          (109, 156),
          (30, 153)]

for pos in coords:
    x = pos[0] - 20
    y = pos[1] - 40
    player0_trail.append((x, y))

for pos in player0_trail:
    x = pos[0] + 40
    y = pos[1]
    player1_trail.append((x, y))

for pos in player0_trail:
    x = pos[0]
    y = pos[1] + 40
    player2_trail.append((x, y))

for pos in player0_trail:
    x = pos[0] + 40
    y = pos[1] + 40
    player3_trail.append((x, y))




WIDTH = 1024
HEIGHT = 650
