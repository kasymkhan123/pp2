import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()
ball = Ball(400, 300, 25, 800, 600)

running = True
while running:
    screen.fill((125, 89, 45))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_UP]:
        ball.move_up()
    if keys[pygame.K_DOWN]:
        ball.move_down()
    if keys[pygame.K_RIGHT]:
        ball.move_right()
    if keys[pygame.K_LEFT]:
        ball.move_left()

    

    ball.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

