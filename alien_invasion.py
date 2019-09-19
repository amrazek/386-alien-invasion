import sys
import pygame
from settings import Settings


def run_game():
    # initialize pygame and create screen surface
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # start main loop for the game
    while True:

        # watch for keyboard and mouse events
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # fill screen with background colo
        screen.fill(ai_settings.bg_color)

        # make most recently drawn screen visible
        pygame.display.flip()


run_game()
