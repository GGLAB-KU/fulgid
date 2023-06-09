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

class Diet:
    def __init__(self):
        self.healthiness = None

def process_event(diet):
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

    # Diet affects pancreatic cancer development
    if diet.healthiness == "more":
        return "less likely to develop pancreatic cancer"
    elif diet.healthiness == "less":
        return "more likely to develop pancreatic cancer"
    else:
        return "no effect on pancreatic cancer development"

diet = Diet()
diet.healthiness = "more"
result = process_event(diet)
print(result)