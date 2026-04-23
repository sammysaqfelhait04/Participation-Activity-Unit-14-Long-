import sys
import pygame
from settings import Settings
from ship import Ship
from game_stat import Gamestat
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stat = self.game_stat(self)
        self.game_stat = Gamestat(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        self.clock = pygame.time.Clock()

        self.game_stat = Gamestat(self.settings.starting_ship_count)
        self.game_active = True

        self.play_button = Button(self, "Play")


        self.arsenal = ShipArsenal(self)
        self.ship = Ship(self, self.arsenal)

        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.arsenal.update_arsenal()
                self.alien_fleet.update_fleet()
                self._check_collisions()

            self._update_screen()
            self.clock.tick(self.settings.FpS)

    def _check_collisions(self):

        self.impact_sound().play()
        self.game_stat.update(collisions)
        self.game_stat.update_level()
             self.alien_fleet.check_collisions(self.arsenal.arsenal)
                            )
    pygame.sprite.groupcollide(
        self.arsenal.arsenal,
        self.alien_fleet.fleet,
        True, True
    )


    if self.alien_fleet.check_destroyed_status():
        self._reset_level()
        self.settings.increase_difficulty()


    if pygame.sprite.spritecollideany(self.ship, self.alien_fleet.fleet):
        self._ship_hit()

    if self.alien_fleet.check_fleet_bottom():
        self._ship_hit()

    def _ship_hit(self):
    if self.game_stat.ship_limit > 0:
        self.game_stat.ship_limit -= 1
        self.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship.rect.midleft = self.screen.get_rect().midleft
    else:
        self.game_active = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self.ship.fire()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN and self.game_active == True:
                    sellf.check_events()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.check_clicked(mouse_pos):
                    self.game

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

        def restart_game(self):
            self.settings.initialize_dynamic_settings()
            self.game_stat.ship_limit = self.settings.starting_ship_count
            self.game_stat.reset_stats()


            self.game_active = True
            self.ship._center_ship()
            self.game_active = True
            pygame.mouse.set_visible(False)


    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        self.ship.draw()
        self.arsenal.draw_arsenal()
        self.alien_fleet.draw_fleet()
        draw HUD(self)
        
        
        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)


        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()