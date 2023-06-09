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

# Ocean waves hit land 
ocean = Ocean() 
land = Land() 
ocean_waves = Wave() 
ocean_waves.strength = 10 
ocean.waves.append(ocean_waves) 
ocean_waves_land = OceanWaves(ocean, ocean_waves) 
land.beaches.append(ocean_waves_land) 

# Ocean water pulls sand off of beaches 
ocean_water = Water() 
ocean_water.strength = 5 
ocean.water.append(ocean_water) 
ocean_water_sand = OceanWater(ocean, ocean_water) 
ocean.sand.append(Sand()) 
ocean_water.carrying.append(ocean.sand[0]) 
water_sand = WaterSand(ocean_water, ocean.sand[0]) 

# Ocean water breaks rocks off of cliffs 
ocean_water.strength = 8 
ocean_water_rocks = OceanWater(ocean, ocean_water) 
ocean.rocks.append(Rock()) 
ocean_water.carrying.append(ocean.rocks[0]) 
water_rock = WaterRock(ocean_water, ocean.rocks[0]) 

# Ocean water carries sand and rocks into the ocean 
ocean_water.strength = 7 
ocean_water.carrying.remove(ocean.sand[0]) 
ocean_water.carrying.remove(ocean.rocks[0]) 
ocean_water.carrying.append(ocean.sand[0]) 
ocean_water.carrying.append(ocean.rocks[0]) 

# Sand and rocks go to other land or the bottom of the ocean 
if ocean_water.strength > 6: 
    ocean.sand.remove(ocean_water.carrying[0]) 
    ocean.rocks.remove(ocean_water.carrying[1]) 
    ocean_water.carrying[0].amount += 1 
    ocean_water.carrying[1].size += 1 
    if ocean_water.carrying[1].size > 5: 
        ocean.rocks.remove(ocean_water.carrying[1]) 
        ocean.rocks.append(Rock()) 
        ocean_water.carrying[1] = ocean.rocks[-1] 

# More ocean water breaks rocks off of cliffs 
ocean_water.strength = 10 
ocean_water.carrying.remove(ocean.rocks[0]) 
ocean_water.carrying.append(ocean.rocks[0]) 

# Check the effect on sand and rocks going to the bottom of the ocean 
if ocean_water.strength > 6: 
    if ocean_water.carrying[0] in ocean.sand: 
        print("more") 
    elif ocean_water.carrying[0] in ocean.rocks: 
        print("less") 
    else: 
        print("no effect")