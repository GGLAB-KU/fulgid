class Ocean: 
    def __init__(self): 
        self.waves = [] 
        self.water = [] 
        self.sand = [] 
        self.rocks = [] 

class Land: 
    def __init__(self): 
        self.beaches = [] 
        self.cliffs = [] 

class Wave: 
    def __init__(self): 
        self.strength = 0 

class Water: 
    def __init__(self): 
        self.strength = 0 
        self.carrying = [] 

class Sand: 
    def __init__(self): 
        self.amount = 0 

class Rock: 
    def __init__(self): 
        self.size = 0 

# Relationship between Ocean and Wave 
class OceanWaves: 
    def __init__(self, ocean, wave): 
        self.ocean = ocean 
        self.wave = wave 

# Relationship between Ocean and Water 
class OceanWater: 
    def __init__(self, ocean, water): 
        self.ocean = ocean 
        self.water = water 

# Relationship between Ocean and Sand 
class OceanSand: 
    def __init__(self, ocean, sand): 
        self.ocean = ocean 
        self.sand = sand 

# Relationship between Ocean and Rock 
class OceanRock: 
    def __init__(self, ocean, rock): 
        self.ocean = ocean 
        self.rock = rock 

# Relationship between Land and Beach 
class LandBeach: 
    def __init__(self, land, beach): 
        self.land = land 
        self.beach = beach 

# Relationship between Land and Cliff 
class LandCliff: 
    def __init__(self, land, cliff): 
        self.land = land 
        self.cliff = cliff 

# Relationship between Water and Sand 
class WaterSand: 
    def __init__(self, water, sand): 
        self.water = water 
        self.sand = sand 

# Relationship between Water and Rock 
class WaterRock: 
    def __init__(self, water, rock): 
        self.water = water 
        self.rock = rock