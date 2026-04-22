"""
Ship module
Author: Sammy Saqfelhait
Purpose: Control player ship
"""

import pygame

class Ship:
    def __init__(self, game, arsenal):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height)
        )

        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen.get_rect().midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

        self.arsenal = arsenal

    def update(self):
    speed = self.settings.ship_speed

    if self.moving_up and self.rect.top > 0:
        self.y -= speed
    if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
        self.y += speed

    self.rect.y = self.y

    def fire(self):
        self.arsenal.fire_bullet()

    def draw(self):
        self.screen.blit(self.image, self.rect)