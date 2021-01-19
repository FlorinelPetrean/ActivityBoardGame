import pygame
from constants import WIDTH, HEIGHT, bg, avatar1, pawn1
from board import Board
from network import Network
from button import Button
from player import Player, Pawn, Avatar

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Activity')
font = pygame.font.SysFont('comicsans', 30)


def draw_teams(screen):
    pygame.draw.rect(screen, (0, 255, 100), (500, 0, 550, 150), 0)
    pygame.draw.rect(screen, (0, 100, 255), (500, 150, 550, 150), 0)
    team0 = font.render("Team Green", True, (0, 0, 0))
    team1 = font.render("Team Blue", True, (0, 0, 0))
    screen.blit(team0, (510, 10))
    screen.blit(team1, (510, 160))

    pygame.draw.rect(screen, (255, 255, 255), (650, 20, 100, 100), 0)  # 0
    pygame.draw.rect(screen, (255, 255, 255), (850, 20, 100, 100), 0)  # 1
    pygame.draw.rect(screen, (255, 255, 255), (650, 20 + 150, 100, 100), 0)  # 2
    pygame.draw.rect(screen, (255, 255, 255), (850, 20 + 150, 100, 100), 0)  # 3


def redrawWindow(screen, game_instance, board, player):
    screen.fill((255, 255, 0))
    board.draw(screen)
    draw_teams(screen)
    for p in game_instance.get_players():
        avatar = pygame.image.load(p.avatar.img)
        avatar = pygame.transform.scale(avatar, (80, 80))
        pawn = pygame.image.load(p.pawn.img)
        pawn = pygame.transform.scale(pawn, (50, 50))
        screen.blit(avatar, p.avatar.get_pos())
        screen.blit(pawn, p.pawn.get_pos())

        username = font.render(p.name, True, (0, 0, 0))
        if p.id == 0:
            screen.blit(username, (650 + 20, 120))
        elif p.id == 1:
            screen.blit(username, (850 + 20, 120))
        elif p.id == 2:
            screen.blit(username, (650 + 20, 20 + 250))
        elif p.id == 3:
            screen.blit(username, (850 + 20, 20 + 250))

    for btn in buttons:
        btn.draw(screen, True)

    pygame.display.update()


FPS = 60

guessButton = Button((0, 255, 0), 520, 560, 150, 50, "You guessed!")
readyButton = Button((255, 255, 255), 520 + 150 + 50, 560, 150, 50, "Ready")

buttons = [guessButton, readyButton]



def main():
    running = True
    clock = pygame.time.Clock()
    deck = []
    n = Network()

    username = "Florin"
    pawn_img = "images/001-satellite dish.png"
    avatar_img = "images/001-satellite dish.png"
    p = n.getP()
    player = Player(p , username, pawn_img, avatar_img)
    # n.send(json.dumps({"u": username, "p": pawn_img, "a": avatar_img}))
    n.send(username + "|" + pawn_img + "|" + avatar_img, False)
    board = Board(bg, deck)

    while running:

        try:
            game_instance = n.send(" ", True)  # get
        except:
            print("Couldn't get game")
            break

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("(" + str(mouse_pos[0]) + ", " + str(mouse_pos[1]) + "), ")
        redrawWindow(screen, game_instance, board, player)


main()
