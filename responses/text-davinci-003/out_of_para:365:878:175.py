class AcidRain:
    def __init__(self):
        self.acidic_waters = True

class Soil:
    def __init__(self):
        self.aluminum = True

class Water:
    def __init__(self):
        self.acidic = False
        self.aluminum = False

class Fish:
    def __init__(self):
        self.dead = False

class Frogs:
    def __init__(self):
        self.dead = False

class Plants:
    def __init__(self):
        self.dead = False

class Insects:
    def __init__(self):
        self.dead = False

class Ecosystem:
    def __init__(self):
        self.balanced = True

# Relationship between classes
acid_rain = AcidRain()
soil = Soil()
water = Water()
fish = Fish()
frogs = Frogs()
plants = Plants()
insects = Insects()
ecosystem = Ecosystem()

# Event
if acid_rain.acidic_waters:
    water.acidic = True
    water.aluminum = soil.aluminum

if water.acidic and water.aluminum:
    fish.dead = True
    frogs.dead = True
    plants.dead = True
    insects.dead = True

if fish.dead and frogs.dead and plants.dead and insects.dead:
    ecosystem.balanced = False