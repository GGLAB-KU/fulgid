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

def event(choking=False):
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
    if choking:
        print("Choking occurs!")
        esophagus.food = None
    else:
        esophagus.food = saliva.chewed_food

    # Food travels into the stomach
    if esophagus.food:
        stomach.food = esophagus.food

    # Acid in the stomach breaks the food down further
    if stomach.food:
        acid.food = stomach.food

    # Food travels into the small intestine
    if acid.food:
        small_intestine.food = acid.food

    # Nutrients from food are absorbed into the blood stream
    if small_intestine.food:
        nutrients.food = small_intestine.food

    # Food travels into the large intestine
    if nutrients.food:
        large_intestine.food = nutrients.food

    # Most of the remaining material is now waste
    if large_intestine.food:
        waste.food = large_intestine.food

    # The waste is eventually removed from the body.
    if waste.food:
        print("Waste removed from the body: {}".format(waste.food))

    if choking and not esophagus.food:
        return "no effect"
    elif not choking and esophagus.food == stomach.food:
        return "no effect"
    elif not choking and esophagus.food != stomach.food:
        return "more"
    elif choking and esophagus.food != stomach.food:
        return "less"

print(event(choking=True)) # Output: no effect
print(event(choking=False)) # Output: no effect