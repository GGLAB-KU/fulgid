class Plant:
    def __init__(self):
        self.alive = True

class Animal:
    def __init__(self):
        self.alive = True

class Soil:
    def __init__(self, depth):
        self.pressure = 0
        self.depth = depth

class Remains:
    def __init__(self):
        self.liquefy = False

class CarbonAtoms:
    def __init__(self):
        self.rearrange = False

class NewSubstance:
    def __init__(self):
        self.created = False

def process(plants, animals, soil, remains, carbon_atoms, new_substance):
    # Plants and animals long ago died
    plants.alive = False
    animals.alive = False

    # They are buried under layers of soil
    soil.pressure += 1

    # Pressure builds over time
    soil.pressure += 1

    # The remains liquefy
    remains.liquefy = True

    # The carbon atoms rearrange to become a new substance.
    if soil.depth > 10:
        carbon_atoms.rearrange = True
    new_substance.created = True

plants = Plant()
animals = Animal()
soil = Soil(depth=15)
remains = Remains()
carbon_atoms = CarbonAtoms()
new_substance = NewSubstance()

process(plants, animals, soil, remains, carbon_atoms, new_substance)

if carbon_atoms.rearrange:
    print("The soil is unusually deep, so more carbon atoms would rearrange.")
else:
    print("The soil depth has no effect on the rearrangement of carbon atoms.")