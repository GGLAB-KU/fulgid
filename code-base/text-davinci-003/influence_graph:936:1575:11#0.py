class Wave:
    def __init__(self):
        self.energy = 0

class Coast:
    def __init__(self):
        self.sediment = 0

class Sediment:
    def __init__(self):
        self.erode_land = False

class Water:
    def __init__(self):
        self.sediment = 0

class Sand:
    def __init__(self):
        self.sediment = 0

def wave_hits_coast(wave, coast):
    coast.sediment += wave.energy

def sediment_erodes_land(sediment):
    sediment.erode_land = True

def water_washes_sediment(water, sediment):
    water.sediment += sediment

def sediment_left_as_sand(sand, sediment):
    sand.sediment += sediment