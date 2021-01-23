import pygame
from constants import WIDTH, HEIGHT, bg
from board import Board
from network import Network
from button import Button
from decks import Decks

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


def redraw_window(screen, game_instance, board, decks, player):
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

    if game_instance.active_player() == player:
        decks.draw(screen)

    for btn in buttons:
        btn.draw(screen, True)

    pygame.display.update()


FPS = 60

guess_button = Button((0, 255, 0), 520, 560, 150, 50, "You guessed!")
ready_button = Button((255, 255, 255), 520 + 150 + 50, 560, 150, 50, "Ready")
deck1_button = Button((0, 0, 0), 343, 429, 100, 150, "")
deck2_button = Button((0, 0, 0), 219, 425, 100, 150, "")
deck3_button = Button((0, 0, 0), 78, 427, 100, 150, "")
deck_buttons = [deck1_button, deck2_button, deck3_button]

buttons = [guess_button, ready_button]


def main():
    running = True
    clock = pygame.time.Clock()
    n = Network()
    username = "Florin"
    pawn_img = "images/pawn/001-satellite dish.png"
    avatar_img = "images/pawn/001-satellite dish.png"
    p = int(n.getP())
    team = 0
    nr_squares = 0
    if p == 2 or p == 3:
        team = 1
    added_player = False
    card_flipped = False
    decks_shuffled = False

    decks = Decks()
    board = Board(bg, decks)

    while running:

        try:
            game_instance = n.send_data("get")  # get
            if decks_shuffled is False:
                decks.shuffle(game_instance.index_deck1, game_instance.index_deck2, game_instance.index_deck3)
                decks_shuffled = True
        except:
            print("Couldn't get game")
            break

        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # clicked on the screen
                mouse_pos = pygame.mouse.get_pos()
                print("(" + str(mouse_pos[0]) + ", " + str(mouse_pos[1]) + "), ")
                if ready_button.isOver(mouse_pos):
                    if added_player is False:
                        added_player = True
                        mesg = "addp|" + username + "|" + pawn_img + "|" + avatar_img
                        print(mesg)
                        n.send_data(mesg)
                    else:
                        mesg = "ready|" + str(p)
                        print(mesg)
                        n.send_data(mesg)

                if p == game_instance.active_player():

                    if deck1_button.isOver(mouse_pos) and card_flipped is False:
                        card_flipped = True
                        nr_squares = 1
                        decks.choose_deck(1)
                    elif deck2_button.isOver(mouse_pos) and card_flipped is False:
                        card_flipped = True
                        nr_squares = 2
                        decks.choose_deck(2)
                    elif deck3_button.isOver(mouse_pos) and card_flipped is False:
                        card_flipped = True
                        nr_squares = 3
                        decks.choose_deck(3)

                    if guess_button.isOver(mouse_pos) and card_flipped is True:
                        card_flipped = False
                        mesg = "play|yes|" + str(team) + "|" + str(nr_squares)
                        print(mesg)
                        n.send_data(mesg)

        redraw_window(screen, game_instance, board, decks, p)


main()
