class AcidRain:
    def __init__(self):
        self.leaches_aluminum = True
        self.dissolves_minerals = True
        self.affects_ph = True
        self.strips_foliage = True

class ClayParticles:
    def __init__(self):
        self.aluminum = 0

class StreamsAndLakes:
    def __init__(self):
        self.aluminum = 0
        self.minerals = 0
        self.nutrients = 0
        self.ph = 0

class Soil:
    def __init__(self):
        self.clay_particles = ClayParticles()
        self.minerals = 0
        self.nutrients = 0
        self.ph = 0

class Plants:
    def __init__(self):
        self.minerals = 0
        self.nutrients = 0
        self.ph = 0

class Animals:
    def __init__(self):
        self.ph = 0

class Trees:
    def __init__(self):
        self.foliage = 0

# Relationship between classes
acid_rain = AcidRain()
soil = Soil()
streams_and_lakes = StreamsAndLakes()
plants = Plants()
animals = Animals()
trees = Trees()

# Acid rain leaches aluminum from clay particles in soil
if acid_rain.leaches_aluminum:
    soil.clay_particles.aluminum += 1

# Aluminum flows into streams and lakes
if acid_rain.leaches_aluminum:
    streams_and_lakes.aluminum += 1

# Acid rain dissolves minerals and nutrients in soil
if acid_rain.dissolves_minerals:
    soil.minerals -= 1
    soil.nutrients -= 1

# Washes them away so plants can't benefit from them
if acid_rain.dissolves_minerals:
    plants.minerals -= 1
    plants.nutrients -= 1

# PH in soil and water gets affected which can kill plants and animals
if acid_rain.affects_ph:
    soil.ph -= 1
    streams_and_lakes.ph -= 1
    plants.ph -= 1
    animals.ph -= 1

# Acid rain in fog at higher elevations can strip foliage off trees.
if acid_rain.strips_foliage:
    trees.foliage -= 1