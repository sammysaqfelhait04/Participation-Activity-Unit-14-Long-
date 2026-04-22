

"""
Alien Fleet module
Author: Sammy Saqfelhait
Purpose: Manage alien fleet and movement
"""

import pygame
from alien import Alien

class AlienFleet:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()

        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
    for row in range(5):
        for col in range(3):
            x = self.game.screen.get_width() - (col * 80)
            y = row * 80
            self._create_alien(x, y)

    def _create_alien(self, x, y):
        alien = Alien(self.game, x, y)
        self.fleet.add(alien)

    def update_fleet(self):
        self.fleet.update()

    def draw_fleet(self):
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, bullets):
        return pygame.sprite.groupcollide(
            bullets,
            self.fleet,
            True,
            True
        )

    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False

    def check_destroyed_status(self):
        return len(self.fleet) == 0