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

soil = Soil()
rain = Rain()
rain.pick_up_carbon_dioxide()
rain.fall_on_soil(soil)
rain.erode_limestone(soil.limestone)