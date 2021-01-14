import pygame


class Game:
    def __init__(self, game_id):
        self.id = game_id
        self.ready = False
        self.player = [0, 1, 2, 3]
        self.team = [0, 1]
        self.team_position = [0, 0]
        self.prev_team_position = [0, 0]
        self.turn = 0
        self.timer = 60
        self.discord_server = ""

    def connected(self):
        return self.ready

    def next_turn(self):
        self.turn = (self.turn + 1) % 4

    def update_timer(self):
        if self.timer < 0:
            self.timer = 0
        else:
            self.timer = self.timer - 1

    def active_player(self, player):
        if (player == 0 and self.turn == 0) or (player == 1 and self.turn == 2) or (player == 2 and self.turn == 1) or (
                player == 3 and self.turn == 3):
            return True
        else:
            return False

    def winner(self):
        winner = -1
        if self.team_position[0] == 40:
            winner = 0
        elif self.team_position[1] == 40:
            winner = 1
        return winner

    def play(self, player, answer):
        guessed = answer[0]
        nr_squares = answer[1]
        if guessed:
            if player == 0 or player == 1:
                self.prev_team_position[0] = self.team_position[0]
                self.team_position[0] = self.team_position[0] + nr_squares
            else:
                self.prev_team_position[1] = self.team_position[1]
                self.team_position[1] = self.team_position[1] + nr_squares
        self.next_turn()

    def turn_back(self, player):
        if player == 0 or player == 1:
            self.team_position[0] = self.prev_team_position[0]
        else:
            self.team_position[1] = self.prev_team_position[1]

    def reset(self):
        self.team_position[0] = 0
        self.team_position[1] = 0
        self.turn = 0
        self.timer = 60
