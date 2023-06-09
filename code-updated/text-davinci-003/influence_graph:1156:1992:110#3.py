class LivingOrganisms:
    def __init__(self, lifespan):
        self.lifespan = lifespan
        self.age = 0
        self.die = False

    def age_organism(self):
        self.age += 1
        if self.age >= self.lifespan:
            self.die = True

class SeaFloor:
    def __init__(self):
        self.matter = True

class Sediment:
    def __init__(self):
        self.layers = []

class CrudeOil:
    def __init__(self):
        self.form = False

class Process:
    def __init__(self, lifespan):
        self.living_organisms = LivingOrganisms(lifespan)
        self.sea_floor = SeaFloor()
        self.sediment = Sediment()
        self.crude_oil = CrudeOil()
    
    def start(self):
        while not self.living_organisms.die:
            self.living_organisms.age_organism()
        if self.living_organisms.die:
            self.sea_floor.matter = True
            self.sediment.layers.append(self.sea_floor.matter)
            if self.living_organisms.age < 10:
                self.sediment.layers = self.sediment.layers * self.living_organisms.age
            else:
                self.sediment.layers = self.sediment.layers * 10
            self.crude_oil.form = True
        if len(self.sediment.layers) < 10:
            return 'less'
        elif len(self.sediment.layers) > 10:
            return 'more'
        else:
            return 'no effect'

process = Process(5)
print(process.start())