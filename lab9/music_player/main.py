import pygame
import os
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 300))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

music_path = os.path.join(r'C:\Users\HUAWEI\OneDrive\Desktop\pp2_reposotory\lab9\music_player\music')
player = MusicPlayer(music_path)

running = True
while running:
    screen.fill((80, 145, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()
            elif event.key == pygame.K_q:
                running = False

    screen.blit(font.render("P Play", True, (0, 0, 0)), (20, 30))
    screen.blit(font.render("S Stop", True, (0, 0, 0)), (20, 70))
    screen.blit(font.render("N Next", True, (0, 0, 0)), (20, 110))
    screen.blit(font.render("B Back", True, (0, 0, 0)), (20, 150))

    screen.blit(font.render("Track: " + player.get_name(), True, (0, 0, 0)), (300, 80))
    screen.blit(font.render("Time: " + str(player.get_time()), True, (0, 0, 0)), (300, 120))

    status = "Playing" if player.playing else "Stopped"
    screen.blit(font.render(status, True, (0, 0, 0)), (300, 160))

    pygame.display.update()
    clock.tick(30)

pygame.quit()