from typing TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class Gamestat:

    def __init__(self, game: AlienInvasion):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()
        
        
        
        
        self.game = game
        self.max_score = 0
        self.ship_limit = game.settings.starting_ship_count
        self.score = 0
        self.level = 1

       def update(self, collisions):
        self._update_score(collisions)
            
        self._update_max_score()
        if self.score > self.max_score:
            self.max_score = self.score
            #print(f"max: {self.max_score}")




        def update(self,collisions):
            update
            for aliens in collisions.values():
                self.score += self.settings.alien_points 
                print(f"basic: {self.score}")

       def new_method(self):
           if self.score > self.max_score:
               self.max_score = self.score



               def update_level(self):
                   self.level += 1
                   print(self.level)




    


        