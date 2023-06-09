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

class Water:
    def __init__(self):
        self.salt = None
    
    def contain_salt(self):
        self.salt = True

def main():
    light = Light()
    soil = Soil()
    air = Air()
    water = Water()
    plant = Plant()

    light.provide_energy()
    plant.absorb_light_energy()
    plant.convert_carbon_dioxide()
    soil.provide_nutrients()
    plant.use_nutrients()
    air.provide_carbon_dioxide()
    plant.produce_glucose()
    if water.contain_salt():
        plant.glucose = False
        plant.oxygen = False
    plant.give_energy()
    plant.release_oxygen()

    if plant.glucose and plant.oxygen:
        print("The presence of salt in water has no effect on the production of sugar and oxygen.")
    elif plant.glucose and not plant.oxygen:
        print("The presence of salt in water results in less oxygen being produced.")
    elif not plant.glucose and plant.oxygen:
        print("The presence of salt in water results in less sugar being produced.")
    else:
        print("The presence of salt in water results in less sugar and oxygen being produced.")

if __name__ == "__main__":
    main()