import pygame
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# DEFENSE: All game objects inherit from pygame.sprite.Sprite. 
# This allows us to group them and use built-in collision detection.

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
        # DEFENSE: TSIS 3 Power-up variables.
        self.lives = 1
        self.shield_active = False
        self.nitro_timer = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        # EXPLANATION: If nitro is active, player moves left/right twice as fast.
        current_speed = 10 if self.nitro_timer > 0 else 5 

        if self.rect.left > 50 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-current_speed, 0)
        if self.rect.right < SCREEN_WIDTH-50 and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(current_speed, 0)
            
        # Decrease nitro timer every frame
        if self.nitro_timer > 0:
            self.nitro_timer -= 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # DEFENSE: Visual feedback for the Shield power-up
        if self.shield_active:
            pygame.draw.circle(surface, (0, 255, 255), self.rect.center, 50, 3)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -100)

    def move(self, speed):
        self.rect.move_ip(0, speed)
        # EXPLANATION: If enemy goes off-screen, reset it to the top.
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()
            return True # Returns True to add to score in main.py
        return False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# DEFENSE: Added Lane Hazards (Obstacles)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # EXPLANATION: Try/Except prevents the game from crashing if obstacle.png is missing.
        try:
            self.image = pygame.transform.scale(pygame.image.load('obstacle.png'), (40, 40))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((100, 100, 100)) # Gray fallback square
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -200)

    def move(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('coin.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -50)

    def move(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# DEFENSE: New PowerUp class handles 3 types of boosts
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.type = ""
        self.reset()

    def reset(self):
        # EXPLANATION: Randomly picks a type and changes its color accordingly.
        self.type = random.choice(["nitro", "shield", "repair"])
        colors = {"nitro": (0, 255, 0), "shield": (0, 255, 255), "repair": (255, 0, 255)}
        self.image.fill(colors[self.type])
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -1000)

    def move(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)