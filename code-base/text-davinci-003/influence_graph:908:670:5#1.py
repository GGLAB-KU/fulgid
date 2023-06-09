class Water:
    def __init__(self):
        self.expansion_percentage = 10
    
    def freeze(self):
        # code to freeze water

class Rock:
    def __init__(self):
        self.cracks = []
    
    def expand_cracks(self, water):
        # code to expand cracks due to water pressure

class Clay:
    def __init__(self):
        self.expansion_percentage = 10
    
    def expand(self):
        # code to expand clay

class Plant:
    def __init__(self):
        self.roots = []
    
    def grow(self, rock):
        # code to grow roots and cause rocks to split apart

# Relationship between classes
water = Water()
rock = Rock()
clay = Clay()
plant = Plant()

water.freeze()
rock.expand_cracks(water)
clay.expand()
plant.grow(rock)