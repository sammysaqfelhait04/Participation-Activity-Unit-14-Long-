


"""
Settings module
Author: Sammy Saqfelhait
Purpose: Store game settings
"""

from pathlib import Path

class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.FpS = 60

        self.bg_file = Path.cwd() / "assets" / "images" / "starbase.png"
        self.difficulty_scale = 1.1
        self.ship_file = Path.cwd() / "assets" / "images" / "ship2(no bg).png"
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / "assets" / "images" / "laserBlast.png"
        self.laser_sound_file = Path.cwd() / "assets" / "sounds" / "laser.mp3"
        self.impact_sound = Path.cwd() / "assets" / "sounds" / "impact.mp3"

        self.bullet_height = 80
        self.bullet_width = 25
        self.bullet_speed = 7
        self.bullets_allowed = 5

self.starting_ship_count = 3

self.alien_file = Path.cwd() / "assets" / "images" / "enmy_4.png"
self.alien_width = 40
self.alien_height = 40
self.fleet_speed = 2
self.fleet_direction = -1
self.fleet_drop_speed = 40



self.button_width = 200
self.button_height = 50
self.button_color = (0, 135, 50)

self.text_color = (255, 255, 255)
self.button_font_size = 48
self.hud_font_size = 20
self.font_file = Path.cwd() / "assets" / "fonts" / "slikscreen"/"slikscreen-Bold.ttf"


def initialize_dynamic_settings(self):
   self.ship_speed = 5
   self.starting_ship_count = 3

   self.bullet_width = 25
   self.bullet_speed = 7
   self.bullet_height = 80
   self.bullet_amount = 5

   self.fleet_speed = 2
   self.fleet_drop_speed = 40

   def increase_difficulty(self):
    self.ship_speed *= self.difficulty_scale
    self.bullet_speed *= self.difficulty_scale
    self.fleet_speed *= self.difficulty_scale