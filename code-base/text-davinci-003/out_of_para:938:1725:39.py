class Plant:
    def __init__(self):
        self.chlorophyll = None
        self.carbon_dioxide = None
        self.nutrients = None
        self.glucose = None
        self.oxygen = None
    
    def absorb_light_energy(self):
        self.chlorophyll = True
    
    def convert_carbon_dioxide(self):
        self.carbon_dioxide = True
    
    def use_nutrients(self):
        self.nutrients = True
    
    def produce_glucose(self):
        self.glucose = True
    
    def give_energy(self):
        self.energy = True
    
    def release_oxygen(self):
        self.oxygen = True

class Light:
    def __init__(self):
        self.energy = None
    
    def provide_energy(self):
        self.energy = True

class Soil:
    def __init__(self):
        self.nutrients = None
    
    def provide_nutrients(self):
        self.nutrients = True

class Air:
    def __init__(self):
        self.carbon_dioxide = None
    
    def provide_carbon_dioxide(self):
        self.carbon_dioxide = True

def main():
    light = Light()
    soil = Soil()
    air = Air()
    plant = Plant()

    light.provide_energy()
    plant.absorb_light_energy()
    plant.convert_carbon_dioxide()
    soil.provide_nutrients()
    plant.use_nutrients()
    air.provide_carbon_dioxide()
    plant.produce_glucose()
    plant.give_energy()
    plant.release_oxygen()

if __name__ == "__main__":
    main()