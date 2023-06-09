class Cell:
    def __init__(self):
        self.centrioles = []
        self.chromosomes = []
        self.spindle_fibers = []
        self.nuclear_membranes = []

class Centriole:
    def __init__(self):
        self.position = None

class Chromosome:
    def __init__(self):
        self.centromere = None
        self.sister_chromatids = []

class SpindleFiber:
    def __init__(self):
        self.attached_chromosomes = []

class NuclearMembrane:
    def __init__(self):
        self.region_of_DNA = None