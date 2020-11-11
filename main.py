# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from constants import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))
pygame.display.set_caption('Activity')


FPS = 60
def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     True

main()