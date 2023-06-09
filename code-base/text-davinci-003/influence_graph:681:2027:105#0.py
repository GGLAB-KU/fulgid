class Animal:
    def __init__(self):
        self.food = 0
        self.hibernation_place = None
        self.heart_rate = 0
        self.breathing_rate = 0
        self.brain_activity = 0
        self.hibernation_mode = False
    
    def eat(self, food):
        self.food += food
    
    def find_hibernation_place(self, place):
        self.hibernation_place = place
    
    def slow_heart_rate(self):
        self.heart_rate -= 1
    
    def slow_breathing_rate(self):
        self.breathing_rate -= 1
    
    def reduce_brain_activity(self):
        self.brain_activity -= 1
    
    def enter_hibernation_mode(self):
        self.hibernation_mode = True

class Environment:
    def __init__(self):
        self.food = 0
        self.hibernation_places = []
    
    def add_food(self, food):
        self.food += food
    
    def add_hibernation_place(self, place):
        self.hibernation_places.append(place)

def hibernation_event(animal, environment):
    # Animal eats large quantities of food
    animal.eat(environment.food)
    
    # Animal finds a place to hibernate
    animal.find_hibernation_place(environment.hibernation_places[0])
    
    # Animal's heart rate and breathing rate drop slowly
    for i in range(10):
        animal.slow_heart_rate()
        animal.slow_breathing_rate()
    
    # Electrical activity in the brain almost ceases completely
    for i in range(10):
        animal.reduce_brain_activity()
    
    # Animal has entered hibernation mode
    animal.enter_hibernation_mode()