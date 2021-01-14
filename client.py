
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

    pygame.draw.rect(screen, (0, 0, 0), (600, 30, 100, 100), 0)
    pygame.draw.rect(screen, (0, 0, 0), (800, 30, 100, 100), 0)
    pass


def redrawWindow(screen, game_instance, board, player):
    screen.fill((255, 255, 0))
    player.avatar.draw(screen)
    player.pawn.draw(screen)
    board.draw(screen)
    draw_teams(screen)
    guessButton.draw(screen, True)
    pygame.display.update()


FPS = 60

guessButton = Button((0, 255, 0), 520, 560, 150, 50, "You guessed!")


def main():
    running = True
    clock = pygame.time.Clock()
    deck = []
    n = Network()
    player = Player(int(n.getP()), "Florin", pawn1, avatar1)

    board = Board(bg, deck)
    game_instance = n.send("get")

    while running:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        redrawWindow(screen, game_instance, board, player)


main()
