class Soil:
    def __init__(self):
        self.limestone = Limestone()

class Limestone:
    def __init__(self):
        self.acid = None

class Rain:
    def __init__(self):
        self.carbon_dioxide = None

    def pick_up_carbon_dioxide(self):
        self.carbon_dioxide = True

    def fall_on_soil(self, soil):
        soil.limestone.acid = self.carbon_dioxide

    def erode_limestone(self, limestone):
        limestone.acid = True

class Coal:
    def __init__(self):
        self.burned = False

    def burn(self):
        self.burned = True

class Boiler:
    def __init__(self):
        self.caverns = 10

    def burn_coal(self, coal):
        coal.burn()
        if coal.burned:
            self.caverns -= 1

soil = Soil()
rain = Rain()
coal = Coal()
boiler = Boiler()

rain.pick_up_carbon_dioxide()
rain.fall_on_soil(soil)
rain.erode_limestone(soil.limestone)

boiler.burn_coal(coal)

if boiler.caverns < 10:
    print("Coal burning caused less/smaller caverns.")
elif boiler.caverns == 10:
    print("Coal burning had no effect on caverns.")