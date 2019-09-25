import pygame


class MuteSound:
    def play(self):
        pass


enemy_explosion_sound = MuteSound()
player_explosion_sound = MuteSound()
player_bullet_sound = MuteSound()


def init_sounds():
    if pygame.mixer:
        global enemy_explosion_sound
        global player_explosion_sound
        global player_bullet_sound

        enemy_explosion_sound = pygame.mixer.Sound("sounds/explosion1.wav") or MuteSound()
        player_explosion_sound = pygame.mixer.Sound("sounds/explosion2.wav") or MuteSound()
        player_bullet_sound = pygame.mixer.Sound("sounds/laser.wav") or MuteSound()
