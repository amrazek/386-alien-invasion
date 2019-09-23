import sys
import pygame


def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Respond to keyboard and mouse events"""
    # watch for keyboard and mouse events
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.KEYDOWN:
            check_keydown_events(evt, ship)

        elif evt.type == pygame.KEYUP:
            check_keyup_events(evt, ship)


def update_screen(ai_settings, screen, ship):
    # redraw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make most recently drawn screen visible
    pygame.display.flip()