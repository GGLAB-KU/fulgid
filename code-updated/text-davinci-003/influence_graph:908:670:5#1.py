class Water:
    def __init__(self):
        self.expansion_percentage = 10
    
    def freeze(self):
        pass
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

class Earth:
    def __init__(self):
        self.temperature = 20
    
    def get_temperature(self):
        return self.temperature
    
    def set_temperature(self, temperature):
        self.temperature = temperature
    
    def get_erosion_effect(self):
        if self.temperature > 20:
            return 'more'
        elif self.temperature < 20:
            return 'less'
        else:
            return 'no effect'

# Relationship between classes
water = Water()
rock = Rock()
clay = Clay()
plant = Plant()
earth = Earth()

# Earth gets hotter
earth.set_temperature(25)

# Check erosion effect
print(earth.get_erosion_effect()) # Output: more