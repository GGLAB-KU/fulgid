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

def start_forest_fire(forest):
    for tree in forest.trees:
        tree.burns = True
    for plant in forest.plants:
        plant.burns = True
        plant.provides_food = False
    for animal in forest.animals:
        animal.escapes = False
        animal.dies_from_smoke = True
        animal.has_food = False

forest = ForestFire()
start_forest_fire(forest)