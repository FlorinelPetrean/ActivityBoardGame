import pygame
from constants import WIDTH, HEIGHT, bg, avatar1, pawn1
from board import Board
from network import Network
from game import Game
from button import Button

from player import Player, Pawn, Avatar

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Activity')


def draw_teams(screen):
    font = pygame.font.SysFont('comicsans', 30)
    pygame.draw.rect(screen, (255, 0, 0), (500, 0, 550, 150), 0)
    pygame.draw.rect(screen, (0, 0, 255), (500, 150, 550, 150), 0)
    team0 = font.render("Team Red", True, (0, 0, 0))
    team1 = font.render("Team Blue", True, (0, 0, 0))
    screen.blit(team0, (510, 10))
    screen.blit(team1, (510, 160))

    pygame.draw.rect(screen, (255, 255, 255), (600, 30, 100, 100), 0)  # 0
    pygame.draw.rect(screen, (255, 255, 255), (800, 30, 100, 100), 0)  # 1
    pygame.draw.rect(screen, (255, 255, 255), (600, 30 + 150, 100, 100), 0)  # 2
    pygame.draw.rect(screen, (255, 255, 255), (800, 30 + 150, 100, 100), 0)  # 3
    pass


def redrawWindow(screen, game_instance, board, player):
    screen.fill((255, 255, 0))
    board.draw(screen)
    draw_teams(screen)
    for p in game_instance.get_players():
        avatar = pygame.image.load(p.avatar.img)
        avatar = pygame.transform.scale(avatar, (80, 80))
        pawn = pygame.image.load(p.pawn.img)
        pawn = pygame.transform.scale(pawn, (50, 50))
        screen.blit(avatar, (p.avatar.x, p.avatar.y))
        screen.blit(pawn, (p.pawn.x, p.pawn.y))
    guessButton.draw(screen, True)

    pygame.display.update()


FPS = 60

guessButton = Button((0, 255, 0), 520, 560, 150, 50, "You guessed!")



class Command:
    def __init__(self, get, reset, player):
        self.get = get
        self.reset = reset
        self.send_player = player


def main():
    running = True
    clock = pygame.time.Clock()
    deck = []
    n = Network()
    player = Player(int(n.getP()), "Florin", "images/001-satellite dish.png", "images/001-satellite dish.png")
    # n.send_object(player)
    board = Board(bg, deck)

    while running:
        game_instance = n.send_object(Command(True, False, None)) #get
        #game_instance.add_player(player)
        try:
            pass
        except:
            running = False
            print("Couldn't get game")
            break
        # if not game_instance.connected():
        #     # n.send_object(player)
        #
        # else:
        n.send_object(Command(False, False, player))

        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        redrawWindow(screen, game_instance, board, player)


main()
