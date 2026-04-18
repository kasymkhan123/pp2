import pygame
import sys
from clock import MickeyClock

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Mickey Clock")

    clock_app = MickeyClock(800, 800)
    fps = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock_app.render(screen)
        pygame.display.flip()
        fps.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()