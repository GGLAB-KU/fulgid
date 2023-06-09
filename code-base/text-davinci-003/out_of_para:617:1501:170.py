class HumanBody:
    def __init__(self):
        self.breath = None

    def take_breath(self):
        self.breath = 'inward'

class Lungs:
    def __init__(self):
        self.alveoli = []

    def transport_air(self):
        for alveolus in self.alveoli:
            alveolus.receive_air()

class Alveoli:
    def __init__(self):
        self.blood = None

    def receive_air(self):
        self.blood = 'oxygen'

class Capillaries:
    def __init__(self):
        self.red_blood_cells = []

    def dissolve_oxygen(self):
        for red_blood_cell in self.red_blood_cells:
            red_blood_cell.bind_oxygen()

class RedBloodCells:
    def __init__(self):
        self.heme = None

    def bind_oxygen(self):
        self.heme = 'protein'

class Tissues:
    def __init__(self):
        self.capillaries = []

    def release_oxygen(self):
        for capillary in self.capillaries:
            capillary.dissolve_oxygen()

human_body = HumanBody()
human_body.take_breath()

lungs = Lungs()
lungs.transport_air()

alveoli = Alveoli()
alveoli.receive_air()

capillaries = Capillaries()
capillaries.dissolve_oxygen()

red_blood_cells = RedBloodCells()
red_blood_cells.bind_oxygen()

tissues = Tissues()
tissues.release_oxygen()