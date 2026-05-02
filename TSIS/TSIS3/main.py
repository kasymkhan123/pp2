import pygame
import json
import db
import game

pygame.init()
dis_width, dis_height = 600, 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake TSIS 3')

# Database init
db.init_db()

# Load settings
try:
    with open("settings.json", "r") as f:
        settings = json.load(f)
except:
    settings = {"snake_color": [0,0,0], "grid": False, "sound": True}

font_title = pygame.font.SysFont("arial", 40, bold=True)
font_small = pygame.font.SysFont("arial", 25)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    dis.blit(img, (x, y))

def save_settings():
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def main_menu():
    # EXPLANATION: State machine architecture. The "state" variable controls which screen we see.
    state = "menu"
    username = ""
    last_score = 0
    last_level = 0
    
    while True:
        dis.fill((200, 200, 200))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit(); return

        if state == "menu":
            draw_text("SNAKE TSIS 3", font_title, (0,0,0), 180, 50)
            draw_text(f"Username: {username}_", font_small, (0,0,255), 180, 150)
            draw_text("Press ENTER to Play", font_small, (0,0,0), 180, 200)
            draw_text("Press L for Leaderboard", font_small, (0,0,0), 180, 240)
            draw_text("Press S for Settings", font_small, (0,0,0), 180, 280)

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and username != "":
                        personal_best = db.get_personal_best(username)
                        # DEFENSE: This launches game.py and waits for the final score!
                        last_score, last_level = game.play_snake(dis, dis_width, dis_height, username, settings, personal_best)
                        db.save_score(username, last_score, last_level)
                        state = "gameover"
                    elif event.key == pygame.K_l: state = "leaderboard"
                    elif event.key == pygame.K_s: state = "settings"
                    elif event.key == pygame.K_BACKSPACE: username = username[:-1]
                    else: username += event.unicode

        elif state == "leaderboard":
            draw_text("TOP 10 LEADERBOARD", font_title, (0,0,0), 100, 20)
            top_10 = db.get_top_10()
            y = 80
            for i, row in enumerate(top_10):
                # row[0] is Name, row[1] is Score, row[2] is Level
                draw_text(f"{i+1}. {row[0]} - Score: {row[1]} (Lvl {row[2]})", font_small, (0,0,0), 100, y)
                y += 25
            draw_text("Press ESC to return", font_small, (255,0,0), 100, y+20)
            
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = "menu"

        elif state == "settings":
            draw_text("SETTINGS", font_title, (0,0,0), 200, 50)
            draw_text(f"1. Grid Overlay (Press G): {settings['grid']}", font_small, (0,0,0), 100, 150)
            draw_text(f"2. Color (Press C to swap): {settings['snake_color']}", font_small, (0,0,0), 100, 200)
            draw_text("Press ESC to Save & Back", font_small, (255,0,0), 100, 300)
            
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        save_settings()
                        state = "menu"
                    if event.key == pygame.K_g:
                        settings['grid'] = not settings['grid']
                    if event.key == pygame.K_c:
                        colors = [[0,0,0], [255,255,255], [255,0,255], [0,0,255]]
                        idx = (colors.index(settings['snake_color']) + 1) % len(colors)
                        settings['snake_color'] = colors[idx]

        elif state == "gameover":
            draw_text("GAME OVER", font_title, (255,0,0), 200, 100)
            draw_text(f"Score: {last_score}  |  Level: {last_level}", font_small, (0,0,0), 180, 180)
            draw_text("Press SPACE to play again", font_small, (0,0,0), 150, 250)
            draw_text("Press ESC for Menu", font_small, (0,0,0), 180, 300)
            
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        personal_best = db.get_personal_best(username)
                        last_score, last_level = game.play_snake(dis, dis_width, dis_height, username, settings, personal_best)
                        db.save_score(username, last_score, last_level)
                    if event.key == pygame.K_ESCAPE:
                        state = "menu"

        pygame.display.update()

if __name__ == "__main__":
    main_menu()