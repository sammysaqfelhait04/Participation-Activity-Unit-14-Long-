

"""
Alien module
Author: Sammy Saqfelhait
Purpose: Create enemy aliens
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_width, self.settings.alien_height)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.fleet_speed
        self.rect.x = self.x

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
        