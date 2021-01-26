import pygame


class Drawing_Board():
    def __init__(self):
        self.color = (255, 255, 255)
        self.x = 500 + 2
        self.y = 0 + 2
        self.width = 524 - 2
        self.height = 550
        self.last_pos = None

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                # self.color = color
                return True
        return False

    def draw_pixel(self, win, pos):
        if self.last_pos is None:
            self.last_pos = pos

        if self.isOver(pos):
            pygame.draw.line(win, (0, 0, 0), self.last_pos, pos)
            self.last_pos = pos

    def draw_pixel1(self, win, last_pos, pos):
        if self.isOver(pos):
            pygame.draw.line(win, (0, 0, 0), last_pos, pos, 1)



