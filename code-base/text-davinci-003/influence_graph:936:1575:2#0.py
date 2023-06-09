class Wave:
    def __init__(self, energy):
        self.energy = energy

class Coast:
    def __init__(self):
        self.sediment = []

class Sediment:
    def __init__(self, size):
        self.size = size

class Water:
    def __init__(self):
        self.sediment = []

class Sand:
    def __init__(self, size):
        self.size = size

# Relationship between classes

# Wave and Coast
def wave_hits_coast(wave, coast):
    coast.sediment.append(wave.energy)

# Coast and Sediment
def coast_erodes_land(coast, sediment):
    coast.sediment.append(sediment)

# Water and Sediment
def water_washes_sediment(water, sediment):
    water.sediment.append(sediment)

# Sediment and Sand
def sediment_left_as_sand(sediment, sand):
    sand.size = sediment.size