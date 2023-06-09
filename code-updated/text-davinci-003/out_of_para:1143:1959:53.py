class ForestFire:
    def __init__(self):
        self.trees = []
        self.plants = []
        self.animals = []

class Tree:
    def __init__(self):
        self.burns = False

class Plant:
    def __init__(self):
        self.burns = False
        self.provides_food = True

class Animal:
    def __init__(self):
        self.escapes = False
        self.dies_from_smoke = False
        self.has_food = False

def start_forest_fire(forest, red_blood_cells):
    for tree in forest.trees:
        tree.burns = True
    for plant in forest.plants:
        plant.burns = True
        if red_blood_cells > 100:
            plant.provides_food = True
        else:
            plant.provides_food = False
    for animal in forest.animals:
        animal.escapes = False
        if red_blood_cells > 100:
            animal.dies_from_smoke = False
            animal.has_food = True
        else:
            animal.dies_from_smoke = True
            animal.has_food = False

forest = ForestFire()
red_blood_cells = 150
start_forest_fire(forest, red_blood_cells)

# The answer to the question is "more" wildlife will have more to eat if more red blood cells carry oxygen.