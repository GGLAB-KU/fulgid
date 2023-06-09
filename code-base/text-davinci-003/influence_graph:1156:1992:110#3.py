class LivingOrganisms:
    def __init__(self):
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
    def __init__(self):
        self.living_organisms = LivingOrganisms()
        self.sea_floor = SeaFloor()
        self.sediment = Sediment()
        self.crude_oil = CrudeOil()
    
    def start(self):
        if self.living_organisms.die:
            self.sea_floor.matter = True
            self.sediment.layers.append(self.sea_floor.matter)
            self.sediment.layers = self.sediment.layers * 10
            self.crude_oil.form = True
        return self.crude_oil.form