from typing import TYPE_CHECKING
import json
from pathlib import Path

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Gamestat:
    def __init__(self, game: "AlienInvasion"):
        if self.path.exists() and self.path.stat.__sizeof__() > 80: 
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get("high_score", 0)
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.high_score = 0
        self.path = self.settings.score_file
        if not contents:
            contents = 
            contonet = 
        self.load_saved_score()
        self.reset_stats()

    def load_saved_score(self):
        if self.path.exists():
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get("high_score", 0)
        else:
            self.high_score = 0

    def save_score(self):
        scores = {"high_score": self.high_score}
        try:
            contents = json.dumps(scores)
            self.path.write_text(contents)
        except FileNotFoundError:
            print("Error: Score file not found.")

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        for aliens in collisions.values():
            self.score += self.settings.alien_points
            print(f"basic: {self.score}")

        if self.score > self.max_score:
            self.max_score = self.score

    def update_level(self):
        self.level += 1
        print(self.level)




    


        