"""
Bullet module
Author: Sammy Saqfelhait
Purpose: Handle bullets
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_width, self.settings.bullet_height)
        )

        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
self.x = float(self.rect.x)

    def update(self):
    self.x += self.settings.bullet_speed
    self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)


        