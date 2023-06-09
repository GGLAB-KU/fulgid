class Food:
    def __init__(self):
        self.nutrients = []

class Stomach:
    def __init__(self):
        self.digestion_process = None

class Bloodstream:
    def __init__(self):
        self.sugars = []

class Insulin:
    def __init__(self):
        self.action = None

class Energy:
    def __init__(self):
        self.source = None

class Fat:
    def __init__(self):
        self.storage = None

class Muscle:
    def __init__(self):
        self.storage = None

class Liver:
    def __init__(self):
        self.storage = None

def process_event():
    food = Food()
    stomach = Stomach()
    bloodstream = Bloodstream()
    insulin = Insulin()
    energy = Energy()
    fat = Fat()
    muscle = Muscle()
    liver = Liver()

    # You eat food
    food.nutrients = ["sugars"]

    # Your stomach digests the food
    stomach.digestion_process = "digestion"

    # Sugars from food enter your bloodstream
    bloodstream.sugars = food.nutrients

    # Insulin helps turn sugars into energy
    insulin.action = "turn sugars into energy"
    energy.source = "sugars"

    # Insulin helps your body store the energy in fat, muscle and liver cells
    insulin.action = "store energy"
    fat.storage = energy
    muscle.storage = energy
    liver.storage = energy

process_event()