class Color:
    def __init__(self, name):
        self.name = name

class Sunlight:
    def __init__(self, intensity):
        self.intensity = intensity

class Leaf:
    def __init__(self, color):
        self.color = color

class Photosynthesis:
    def __init__(self, leaf, sunlight):
        self.leaf = leaf
        self.sunlight = sunlight

    def glucose_production(self):
        if self.sunlight.intensity > 80:
            return "more"
        elif self.sunlight.intensity < 50:
            return "less"
        else:
            return "no effect"

class Glucose:
    def __init__(self, photosynthesis):
        self.photosynthesis = photosynthesis

    def oxygen_production(self):
        if self.photosynthesis.sunlight.intensity > 80:
            return "more"
        elif self.photosynthesis.sunlight.intensity < 50:
            return "less"
        else:
            return "no effect"

class Plant:
    def __init__(self, glucose):
        self.glucose = glucose

green = Color("green")
sunlight = Sunlight(90)
leaf = Leaf(green)
photosynthesis = Photosynthesis(leaf, sunlight)
glucose = Glucose(photosynthesis)
plant = Plant(glucose)

print("If there are more sunny days, the effect on glucose production will be:", photosynthesis.glucose_production())
print("If there are more sunny days, the effect on oxygen production will be:", glucose.oxygen_production())