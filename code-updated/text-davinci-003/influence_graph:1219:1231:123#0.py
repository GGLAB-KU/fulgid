class Plant:
    def __init__(self, size):
        self.size = size

class Soil:
    def __init__(self, fertility):
        self.fertility = fertility

class Environment:
    def __init__(self):
        self.plants = []
        self.soil = Soil(fertility=0)
    
    def add_plant(self, plant):
        self.plants.append(plant)
    
    def update_soil_fertility(self):
        for plant in self.plants:
            if plant.size == 'small':
                self.soil.fertility += 1
            elif plant.size == 'large':
                self.soil.fertility += 2
    
    def grow_plants(self):
        for plant in self.plants:
            if self.soil.fertility > 0:
                if plant.size == 'small':
                    plant.size = 'large'
                elif plant.size == 'large':
                    self.plants.append(Plant(size='tree'))

# Create environment
environment = Environment()

# Add plants
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))

# Add grass
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))
environment.add_plant(Plant(size='small'))

# Update soil fertility
environment.update_soil_fertility()

# Grow plants
environment.grow_plants()

# Check effect of grass gathering
if len(environment.plants) == 10:
    print('no effect')
elif len(environment.plants) < 10:
    print('less')
else:
    print('more')