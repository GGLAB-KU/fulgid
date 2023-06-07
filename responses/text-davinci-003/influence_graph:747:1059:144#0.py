class Water:
    def __init__(self):
        self.surface = True

class Soil:
    def __init__(self):
        self.water = None

class Rock:
    def __init__(self):
        self.water = None
        self.cave = False

class Cave:
    def __init__(self):
        self.rock = None
        self.cavern = False

class Cavern:
    def __init__(self):
        self.cave = None

# Relationship between the classes
water = Water()
soil = Soil()
rock = Rock()
cave = Cave()
cavern = Cavern()

soil.water = water
rock.water = water
cave.rock = rock
cavern.cave = cave