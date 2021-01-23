from constants import deck1, deck2, deck3, decks_pos, topdeck_pos
import random

class Decks:
    def __init__(self):
        self.deck1 = deck1
        self.deck2 = deck2
        self.deck3 = deck3
        self.chosen_deck = 0

    def choose_deck(self, deck_nr):
        self.chosen_deck = deck_nr

    def topdeck(self):
        show_card = self.deck1[0]
        if self.chosen_deck == 1:
            show_card = self.deck1[0]
        if self.chosen_deck == 2:
            show_card = self.deck2[0]
        elif self.chosen_deck == 3:
            show_card = self.deck3[0]
        return show_card

    def move_topdeck(self):
        if self.chosen_deck == 1:
            topdeck = deck1[0]
            deck1.pop(0)
            deck1.append(topdeck)
        if self.chosen_deck == 2:
            topdeck = deck1[0]
            deck2.pop(0)
            deck2.append(topdeck)
        elif self.chosen_deck == 3:
            topdeck = deck1[0]
            deck3.pop(0)
            deck3.append(topdeck)
        self.chosen_deck = 0

    def shuffle(self, index_deck1, index_deck2, index_deck3):
        new_deck1 = []
        new_deck2 = []
        new_deck3 = []
        for i in range(10):
            new_deck1.append(self.deck1[index_deck1[i]])
            new_deck2.append(self.deck2[index_deck2[i]])
            new_deck3.append(self.deck3[index_deck3[i]])

        self.deck1 = new_deck1
        self.deck2 = new_deck2
        self.deck3 = new_deck3



    def draw(self, screen):
        if self.chosen_deck != 0:
            screen.blit(self.topdeck(), topdeck_pos[self.chosen_deck - 1])





