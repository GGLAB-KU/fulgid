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
    def __init__(self, leaf):
        self.leaf = leaf

class Glucose:
    def __init__(self, photosynthesis):
        self.photosynthesis = photosynthesis

class Plant:
    def __init__(self, glucose):
        self.glucose = glucose

green = Color("green")
sunlight = Sunlight(100)
leaf = Leaf(green)
photosynthesis = Photosynthesis(leaf)
glucose = Glucose(photosynthesis)
plant = Plant(glucose)