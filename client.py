import pygame
from constants import WIDTH, HEIGHT, bg
from board import Board
from network import Network
from button import Button
from decks import Decks
from drawing_board import Drawing_Board

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Activity')
font = pygame.font.SysFont('comicsans', 30)
timer_font = pygame.font.SysFont('comicsans', 70)


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


def redraw_window(screen, game_instance, board, decks, scribble_board, player):
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
            screen.blit(username, (650 + 20, 125))
        elif p.id == 1:
            screen.blit(username, (850 + 20, 125))
        elif p.id == 2:
            screen.blit(username, (650 + 20, 25 + 250))
        elif p.id == 3:
            screen.blit(username, (850 + 20, 25 + 250))

    if player == game_instance.active_player():
        decks.draw(screen)

    screen.blit(timer_text, (260, 60))

    for btn in buttons:
        btn.draw(screen, True)

    if game_instance.on_scribble_squares():
        scribble_board.draw(screen, True)
        last_pos = None
        for pos in game_instance.scribble_pixels:
            if last_pos is not None:
                scribble_board.draw_pixel1(screen, last_pos, pos)
            last_pos = pos

        for lines in game_instance.drawn_lines:
            last_pos = None
            for pos in lines:
                if last_pos is not None:
                    scribble_board.draw_pixel1(screen, last_pos, pos)
                last_pos = pos

    pygame.display.update()


guess_button = Button((0, 255, 0), 520, 560, 150, 50, "You guessed!")
ready_button = Button((255, 255, 255), 520 + 150 + 10, 560, 150, 50, "Ready")
takeback_button = Button((0, 255, 255), 520 + 300 + 20, 560, 150, 50, "Takeback")

deck1_button = Button((0, 0, 0), 343, 429, 100, 150, "")
deck2_button = Button((0, 0, 0), 219, 425, 100, 150, "")
deck3_button = Button((0, 0, 0), 78, 427, 100, 150, "")
deck_buttons = [deck1_button, deck2_button, deck3_button]

buttons = [guess_button, ready_button, takeback_button]

FPS = 60

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
timer_text = timer_font.render("60", True, (0, 0, 0))


def main():
    global timer_text
    running = True
    clock = pygame.time.Clock()
    n = Network()
    username = "Florin"
    pawn_img = "images/pawn/001-satellite dish.png"
    avatar_img = "images/pawn/001-satellite dish.png"
    p = int(n.getP())
    team = 0
    if p == 2 or p == 3:
        team = 1

    nr_squares = 0
    timer = 60
    added_player = False
    card_flipped = False
    decks_shuffled = False
    timer_on = False
    mouse_pressed = False
    decks = Decks()
    board = Board(bg, decks)
    scribble_board = Drawing_Board()

    while running:

        try:
            game_instance = n.send_data("get")  # get
        except:
            print("Couldn't get game")
            break
        if decks_shuffled is False:
            decks.shuffle(game_instance.index_deck1, game_instance.index_deck2, game_instance.index_deck3)
            decks_shuffled = True
        timer_on = game_instance.timer_on

        if game_instance.winner() != -1:
            winner_font = pygame.font.SysFont("comicsans", 90)
            if game_instance.winner() == 0:
                winner_text = winner_font.render("Team Green WON", True, (0, 0, 0))
            else:
                winner_text = winner_font.render("Team Blue WON", True, (0, 0, 0))
            screen.blit(winner_text,
                        (WIDTH / 2 - winner_text.get_width() / 2, HEIGHT / 2 - winner_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5000)
            mesg = "reset"
            n.send_data(mesg)

        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False

            if event.type == timer_event:
                if timer_on is True:
                    if timer > 0:
                        timer = timer - 1
                        timer_text = timer_font.render(str(timer), True, (0, 0, 0))
                    else:
                        timer = 0
                        timer_text = timer_font.render("0", True, (0, 0, 0))
                        card_flipped = False
                        decks.choose_deck(0)
                        mesg = "play|no|" + str(team) + "|" + "0"
                        print(mesg)
                        n.send_data(mesg)
                else:
                    timer = 60
                    timer_text = timer_font.render(str(timer), True, (0, 0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mesg = "scribble|reset"
                    n.send_data(mesg)

            if event.type == pygame.MOUSEBUTTONUP:
                mesg = "scribble|stop"
                n.send_data(mesg)

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                # print("(" + str(mouse_pos[0]) + ", " + str(mouse_pos[1]) + "), ")
                if event.buttons[0] and p == game_instance.active_player() \
                        and game_instance.on_scribble_squares() and game_instance.timer_on:
                    if scribble_board.isOver(mouse_pos):
                        mesg = "scribble|" + str(mouse_pos[0]) + "|" + str(mouse_pos[1])
                        print(mesg)
                        n.send_data(mesg)

            if event.type == pygame.MOUSEBUTTONDOWN:  # clicked on the screen
                mouse_pos = pygame.mouse.get_pos()
                print("(" + str(mouse_pos[0]) + ", " + str(mouse_pos[1]) + "), ")
                if ready_button.isOver(mouse_pos):
                    if added_player is False:
                        added_player = True
                        mesg = "addp|" + username + "|" + pawn_img + "|" + avatar_img
                        print(mesg)
                        n.send_data(mesg)
                    elif p == game_instance.active_player() and card_flipped is True:
                        mesg = "ready|" + str(p)
                        print(mesg)
                        n.send_data(mesg)

                if takeback_button.isOver(mouse_pos):
                    mesg = "takeback|" + str(p)
                    print(mesg)
                    n.send_data(mesg)

                # actions available only to the active player
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

                    if guess_button.isOver(mouse_pos) and card_flipped is True and timer_on:
                        card_flipped = False
                        decks.choose_deck(0)
                        mesg = "play|yes|" + str(team) + "|" + str(nr_squares)
                        print(mesg)
                        n.send_data(mesg)

        redraw_window(screen, game_instance, board, decks, scribble_board, p)


main()
