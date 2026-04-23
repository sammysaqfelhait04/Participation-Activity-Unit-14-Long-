import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        
        # Font settings for scoring information.
        self.font = pygame.font.Font(self.settings.font_file, 
                                     self.settings.HUD_font_size)
        
        self.padding = 20
        self.update_scores()
        self.setup_life_image()
        self.update_level()

    def update_scores(self) -> None:
        self.update_hi_score() # Note: This method was being called in screenshot 569
        self._update_score()
        self._update_max_score()

    def _update_score(self) -> None:
        """Render the current score into an image."""
        score_str = f'Score: {self.game_stats.score:,.0f}'
        self.score_image = self.font.render(score_str, True,
                                            self.settings.text_color, None)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.padding

    def _update_max_score(self) -> None:
        """Render the max score into an image."""
        max_score_str = f'Max-Score: {self.game_stats.max_score:,.0f}'
        self.max_score_image = self.font.render(max_score_str, True,
                                                self.settings.text_color, None)
        
        # Position the max score below the current score.
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.score_rect.bottom + self.padding

    # These methods were called in __init__ but the full implementation 
    # was scrolled off-screen in the screenshots:
    def update_hi_score(self):
        pass

    def setup_life_image(self):
        pass

    def update_level(self):
        pass