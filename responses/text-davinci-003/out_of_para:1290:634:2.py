class Participant:
    def __init__(self, name):
        self.name = name

class PancakeMix:
    def __init__(self):
        self.mix_ingredients = []

class Griddle:
    def __init__(self):
        self.heat_level = 0

class Pancake:
    def __init__(self):
        self.batter = None
        self.cooked = False
        self.toppings = []

class Recipe:
    def __init__(self):
        self.steps = []

class Event:
    def __init__(self):
        self.participants = []
        self.recipe = Recipe()
        self.pancake_mix = PancakeMix()
        self.griddle = Griddle()
        self.pancake = Pancake()
    
    def add_participant(self, participant):
        self.participants.append(participant)
    
    def mix_pancake_mix(self):
        # mix pancake mix with water
        pass
    
    def heat_griddle(self):
        # heat a griddle
        pass
    
    def pour_batter(self):
        # pour a circle of batter in the griddle
        pass
    
    def flip_pancake(self):
        # when most of the bubbles pop on the surface, flip
        pass
    
    def cook_pancake(self):
        # cook to desired color
        pass
    
    def apply_toppings(self):
        # apply butter, syrup and enjoy
        pass
    
    def run_event(self):
        self.mix_pancake_mix()
        self.heat_griddle()
        self.pour_batter()
        self.flip_pancake()
        self.cook_pancake()
        self.apply_toppings()