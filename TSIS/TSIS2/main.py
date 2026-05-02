import pygame, sys
from pygame.locals import *

# DEFENSE: Importing custom modules to keep structure clean
import persistence
import ui
from racer import Player, Enemy, Obstacle, Coin, PowerUp

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer - Extended")

# Assets
background = pygame.image.load("AnimatedStreet.png")
crash_sound = pygame.mixer.Sound("crash.wav")
background_sound = pygame.mixer.Sound("background.wav")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# DEFENSE: Custom Pygame Event to increase difficulty over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000) # Triggers every 1 second

# Load JSON Data
settings = persistence.load_data("settings.json", {"sound": True, "difficulty": "Normal"})
leaderboard = persistence.load_data("leaderboard.json", [])

class Stages:
    def __init__(self):
        # EXPLANATION: State machine. self.state controls which screen is currently visible.
        self.state = "intro" 
        self.counter = 0
        self.distance = 0
        self.score = 0
        self.speed = 3
        self.username = ""
        
        # Menu Buttons
        self.btn_play = pygame.Rect(100, 200, 200, 50)
        self.btn_settings = pygame.Rect(100, 270, 200, 50)
        self.btn_leaders = pygame.Rect(100, 340, 200, 50)

    def intro(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if self.btn_play.collidepoint(event.pos): self.state = "username"
                elif self.btn_settings.collidepoint(event.pos): self.state = "settings"
                elif self.btn_leaders.collidepoint(event.pos): self.state = "leaderboard"

        DISPLAYSURF.blit(background, (0, 0))
        ui.draw_button(DISPLAYSURF, self.btn_play, "PLAY", font_small, GRAY, BLACK)
        ui.draw_button(DISPLAYSURF, self.btn_settings, "SETTINGS", font_small, GRAY, BLACK)
        ui.draw_button(DISPLAYSURF, self.btn_leaders, "LEADERBOARD", font_small, GRAY, BLACK)

    def get_username(self):
        """DEFENSE: Records keystrokes to get player name before starting."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN and self.username != "":
                    self.reset_game()
                    self.state = "main"
                elif event.key == K_BACKSPACE:
                    self.username = self.username[:-1]
                else:
                    self.username += event.unicode

        DISPLAYSURF.fill(WHITE)
        ui.draw_text(DISPLAYSURF, "Enter Name:", font_small, BLACK, 140, 250)
        ui.draw_text(DISPLAYSURF, self.username + "_", font, RED, 100, 300)

    def settings_screen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # EXPLANATION: Save settings immediately to JSON when leaving screen
                    persistence.save_data("settings.json", settings)
                    self.state = "intro"
                if event.key == K_s:
                    settings["sound"] = not settings["sound"]
                if event.key == K_d:
                    diffs = ["Easy", "Normal", "Hard"]
                    settings["difficulty"] = diffs[(diffs.index(settings["difficulty"]) + 1) % 3]

        DISPLAYSURF.fill(WHITE)
        ui.draw_text(DISPLAYSURF, "SETTINGS (Press ESC)", font_small, BLACK, 80, 100)
        ui.draw_text(DISPLAYSURF, f"Sound (Press S): {settings['sound']}", font_small, BLACK, 60, 200)
        ui.draw_text(DISPLAYSURF, f"Difficulty (Press D): {settings['difficulty']}", font_small, BLACK, 60, 250)

    def leaderboard_screen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.state = "intro"

        DISPLAYSURF.fill(WHITE)
        ui.draw_text(DISPLAYSURF, "TOP 10 SCORES (Press ESC)", font_small, BLACK, 50, 50)
        
        # EXPLANATION: lambda x: x["score"] tells python to sort the dictionaries based on the 'score' key. reverse=True makes it highest to lowest.
        sorted_lb = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:10]
        for i, entry in enumerate(sorted_lb):
            text = f"{i+1}. {entry['name']} - {entry['score']}"
            ui.draw_text(DISPLAYSURF, text, font_small, BLACK, 50, 100 + i*30)

    def main_game(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            # DEFENSE: Difficulty scaling. Speed increases every second.
            if event.type == INC_SPEED:
                self.speed += 0.5

        if settings["sound"] and not pygame.mixer.get_busy():
            background_sound.play(-1)
        elif not settings["sound"]:
            background_sound.stop()

        DISPLAYSURF.blit(background, (0, 0))
        self.distance += self.speed / 10

        P1.update()
        if E1.move(self.speed): self.score += 1 # Added point if evaded
        C1.move(self.speed)
        O1.move(self.speed)
        PW.move(self.speed)

        # EXPLANATION: sprite.collide_rect checks if two rectangular hitboxes overlap.
        if pygame.sprite.collide_rect(P1, C1):
            self.counter += 1
            self.score += 5
            C1.reset()
            
        # DEFENSE: Applying power-up logic based on type.
        if pygame.sprite.collide_rect(P1, PW):
            if PW.type == "nitro": P1.nitro_timer = 180 # 3 seconds (60 frames * 3)
            elif PW.type == "shield": P1.shield_active = True
            elif PW.type == "repair": P1.lives = min(2, P1.lives + 1)
            PW.reset()

        for entity in all_sprites:
            entity.draw(DISPLAYSURF)
        
        # Draw HUD (Heads Up Display)
        ui.draw_text(DISPLAYSURF, f"Score: {self.score + int(self.distance)}", font_small, BLACK, 10, 10)
        ui.draw_text(DISPLAYSURF, f"Coins: {self.counter}", font_small, BLACK, 10, 40)
        ui.draw_text(DISPLAYSURF, f"Lives: {P1.lives}", font_small, RED, 10, 70) 
        if P1.nitro_timer > 0:
            ui.draw_text(DISPLAYSURF, "NITRO!", font_small, (0, 255, 0), 10, 100)

        # DEFENSE: Crash Logic against Traffic OR Obstacles
        if pygame.sprite.collide_rect(P1, E1) or pygame.sprite.collide_rect(P1, O1):
            if P1.shield_active:
                P1.shield_active = False # Shield saves us once
                if pygame.sprite.collide_rect(P1, E1): E1.reset()
                else: O1.reset()
            else:
                P1.lives -= 1
                if P1.lives <= 0:
                    background_sound.stop()
                    if settings["sound"]: crash_sound.play()
                    
                    # DEFENSE: Save top score to JSON on death
                    final_score = self.score + int(self.distance)
                    leaderboard.append({"name": self.username, "score": final_score})
                    persistence.save_data("leaderboard.json", leaderboard)
                    
                    self.state = "game_over"

    def game_over(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                self.state = "intro"

        DISPLAYSURF.fill(RED)
        ui.draw_text(DISPLAYSURF, "Game Over", font, BLACK, 30, 250)
        ui.draw_text(DISPLAYSURF, "Click anywhere to Menu", font_small, WHITE, 80, 350)

    def reset_game(self):
        # EXPLANATION: Sets everything back to zero before a new run
        self.score = 0
        self.counter = 0
        self.distance = 0
        diff_speeds = {"Easy": 2, "Normal": 3, "Hard": 5}
        self.speed = diff_speeds[settings["difficulty"]]
        
        P1.rect.center = (160, 520)
        P1.lives = 1
        P1.shield_active = False
        E1.reset()
        C1.reset()
        O1.reset()
        PW.reset()

    def state_manager(self):
        if self.state == "intro": self.intro()
        elif self.state == "username": self.get_username()
        elif self.state == "settings": self.settings_screen()
        elif self.state == "leaderboard": self.leaderboard_screen()
        elif self.state == "main": self.main_game()
        elif self.state == "game_over": self.game_over()

P1 = Player()
E1 = Enemy()
C1 = Coin()
O1 = Obstacle() 
PW = PowerUp()  

# Grouping sprites
all_sprites = pygame.sprite.Group(P1, E1, C1, O1, PW)
game = Stages()

while True:
    game.state_manager()
    pygame.display.update()
    FramePerSec.tick(FPS)