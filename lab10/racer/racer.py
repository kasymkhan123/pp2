import pygame, sys, random
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Assets
background = pygame.image.load("racer/AnimatedStreet.png")
crash_sound = pygame.mixer.Sound("racer/crash.wav")
background_sound = pygame.mixer.Sound("racer/background.wav")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Speed event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Stages:
    def __init__(self):
        self.state = "intro"

        self.start_button = pygame.Rect(100, 250, 200, 80)
        self.start_text = font.render("START", True, RED)
        self.counter = 0


    def intro(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    self.reset_game()
                    self.state = "main"

        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(self.start_text, (110, 260))

    def main_game(self):
        global SPEED

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == INC_SPEED:
                SPEED += 0.5

        DISPLAYSURF.blit(background, (0, 0))

        score_text = font_small.render(str(SCORE), True, BLACK)
        DISPLAYSURF.blit(score_text, (10, 10))

        all_sprites.update()
        E1.move()
        C1.move()

        if pygame.sprite.spritecollideany(P1, coins):
            self.counter += 1
            C1.reset()

        for entity in all_sprites:
            entity.draw(DISPLAYSURF)
        
        coin_text = font_small.render(f"Coins: {self.counter}", True, BLACK)
        DISPLAYSURF.blit(coin_text, (10, 40))   

        
        
        background_sound.play(-1)
        if pygame.sprite.spritecollideany(P1, enemies):
            background_sound.stop()
            crash_sound.play()
            self.state = "game_over"

    

        
        

    def game_over(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                self.state = "intro"

        DISPLAYSURF.fill(RED)
        text = font.render("Game Over", True, BLACK)
        DISPLAYSURF.blit(text, (30, 250))

    def reset_game(self):
        global SCORE, SPEED
        SCORE = 0
        SPEED = 3
        self.counter = 0
        P1.rect.center = (160, 520)
        E1.reset()
        C1.reset()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "main":
            self.main_game()
        elif self.state == "game_over":
            self.game_over()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('racer/coin.png'), (64, 64))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)   

        







# Init objects
P1 = Player()
E1 = Enemy()
C1 = Coin()


enemies = pygame.sprite.Group(E1)
all_sprites = pygame.sprite.Group(P1, E1)
coins = pygame.sprite.Group(C1)
all_sprites.add(C1)

game = Stages()

# Main loop
while True:
    game.state_manager()
    pygame.display.update()
    FramePerSec.tick(FPS)