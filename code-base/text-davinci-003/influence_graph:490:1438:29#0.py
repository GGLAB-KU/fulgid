class Participant:
    def __init__(self):
        pass

class Mouth(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class Saliva(Participant):
    def __init__(self):
        super().__init__()
        self.chewed_food = None

class Esophagus(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class Stomach(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class Acid(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class SmallIntestine(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class Nutrients(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class LargeIntestine(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

class Waste(Participant):
    def __init__(self):
        super().__init__()
        self.food = None

def event():
    mouth = Mouth()
    saliva = Saliva()
    esophagus = Esophagus()
    stomach = Stomach()
    acid = Acid()
    small_intestine = SmallIntestine()
    nutrients = Nutrients()
    large_intestine = LargeIntestine()
    waste = Waste()

    # Food is put into mouth
    mouth.food = "food"

    # Food is chewed and mixed with saliva (spit)
    saliva.chewed_food = mouth.food

    # Food travels down the esophagus (throat)
    esophagus.food = saliva.chewed_food

    # Food travels into the stomach
    stomach.food = esophagus.food

    # Acid in the stomach breaks the food down further
    acid.food = stomach.food

    # Food travels into the small intestine
    small_intestine.food = acid.food

    # Nutrients from food are absorbed into the blood stream
    nutrients.food = small_intestine.food

    # Food travels into the large intestine
    large_intestine.food = nutrients.food

    # Most of the remaining material is now waste
    waste.food = large_intestine.food

    # The waste is eventually removed from the body.
    print("Waste removed from the body: {}".format(waste.food))

event()