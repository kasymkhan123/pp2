import pygame


class Ball:
    def __init__(self, x, y, r, w, h):
        self.x = x
        self.y = y
        self.r = r
        self.w = w
        self.h = h
        self.step = 10

    def move_left(self):
        if self.x - self.step - self.r >= 0:
            self.x -= self.step

    def move_right(self):
        if self.x + self.step + self.r <= self.w:
            self.x += self.step

    def move_up(self):
        if self.y - self.step - self.r >= 0:
            self.y -= self.step

    def move_down(self):
        if self.y + self.step + self.r <= self.h:
            self.y += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, (180, 181, 182), (self.x, self.y), self.r)