#Classes

class Mushroom:
    def __init__(self, spores):
        self.spores = spores

class Spore:
    def __init__(self, environment):
        self.environment = environment

class Environment:
    def __init__(self, hospitable):
        self.hospitable = hospitable

#Relationships

class AdultMushroom:
    def __init__(self, spores):
        self.spores = spores

class SporeRelease:
    def __init__(self, spores, process):
        self.spores = spores
        self.process = process

class Wind:
    def __init__(self, spores):
        self.spores = spores

class Germination:
    def __init__(self, spores, soil):
        self.spores = spores
        self.soil = soil

class Growth:
    def __init__(self, mushroom):
        self.mushroom = mushroom

#Process

def process():
    adult_mushroom = AdultMushroom(spores)
    spore_release = SporeRelease(spores, process)
    wind = Wind(spores)
    environment = Environment(hospitable)
    germination = Germination(spores, soil)
    growth = Growth(mushroom)
    adult_mushroom.spores = spore_release.spores
    spore_release.process()
    wind.spores = spore_release.spores
    environment.hospitable = wind.spores
    germination.spores = environment.hospitable
    germination.soil = environment.hospitable
    growth.mushroom = germination.spores
    adult_mushroom.spores = growth.mushroom
    process()