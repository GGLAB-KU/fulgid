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

class Iceberg:
    def __init__(self):
        self.water_level = 0

def wave_hits_coast(wave, coast):
    coast.sediment += wave.energy

def sediment_erodes_land(sediment):
    sediment.erode_land = True

def water_washes_sediment(water, sediment):
    water.sediment += sediment

def sediment_left_as_sand(sand, sediment):
    sand.sediment += sediment

def lower_water_level(iceberg, water):
    water_level = iceberg.water_level
    water_level -= 1
    iceberg.water_level = water_level

def erosion_by_ocean(iceberg):
    if iceberg.water_level < 0:
        return 'more'
    else:
        return 'no effect'

# Example usage
wave = Wave()
coast = Coast()
sediment = Sediment()
water = Water()
sand = Sand()
iceberg = Iceberg()

wave.energy = 10
wave_hits_coast(wave, coast)
sediment_erodes_land(sediment)
water_washes_sediment(water, sediment)
sediment_left_as_sand(sand, sediment)

lower_water_level(iceberg, water)
print(erosion_by_ocean(iceberg)) # Output: more