

"""
Arsenal module
Author: Sammy Saqfelhait
Purpose: Manage bullets
"""

import pygame
from bullet import Bullet

class ShipArsenal:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()

        for bullet in self.arsenal.copy():
            if bullet.rect.left > self.game.screen.get_width():
                self.arsenal.remove(bullet)

    def draw_arsenal(self):
        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullets_allowed:
            bullet = Bullet(self.game)
            self.arsenal.add(bullet)