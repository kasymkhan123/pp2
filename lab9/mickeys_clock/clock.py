import pygame
import datetime
import os


class MickeyClock:
    def __init__(self, w, h):
        self.center = (w // 2, h // 2)

        base = os.path.dirname(os.path.abspath(__file__))
        img = os.path.join(base, "images")

        self.bg = pygame.image.load(os.path.join(img, "clock.png"))
        self.bg = pygame.transform.scale(self.bg, (w, h))

        self.body = pygame.image.load(os.path.join(img, "mikkey.png")).convert_alpha()
        self.body = pygame.transform.scale(self.body, (380, 500))
        self.body_rect = self.body.get_rect(center=self.center)

        self.min_hand = pygame.image.load(os.path.join(img, "hand_right_centered.png")).convert_alpha()
        self.min_hand = pygame.transform.scale(self.min_hand, (200, 300))

        self.sec_hand = pygame.image.load(os.path.join(img, "hand_left_centered.png")).convert_alpha()
        self.sec_hand = pygame.transform.scale(self.sec_hand, (190, 280))

    def draw_hand(self, surface, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=self.center)
        surface.blit(rotated, rect)

    def render(self, surface):
        surface.blit(self.bg, (0, 0))
        surface.blit(self.body, self.body_rect)

        now = datetime.datetime.now()

        sec_angle = -now.second * 6
        min_angle = -now.minute * 6

        self.draw_hand(surface, self.sec_hand, sec_angle)
        self.draw_hand(surface, self.min_hand, min_angle)