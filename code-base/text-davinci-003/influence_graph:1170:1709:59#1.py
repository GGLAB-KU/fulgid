class Cell:
    def __init__(self):
        self.chromosomes = []
        self.centrioles = []
        self.nuclear_membranes = []
        self.cell_membranes = []

class Chromosome:
    def __init__(self):
        self.chromatids = []

class Centriole:
    def __init__(self):
        self.position = None

class NuclearMembrane:
    def __init__(self):
        self.position = None

class CellMembrane:
    def __init__(self):
        self.position = None

def prophase(cell):
    for chromosome in cell.chromosomes:
        chromosome.visible = True

def centrioles_separation(cell):
    for centriole in cell.centrioles:
        centriole.position = 'opposite poles'

def metaphase(cell):
    for chromosome in cell.chromosomes:
        chromosome.position = 'center'

def anaphase(cell):
    for chromosome in cell.chromosomes:
        for chromatid in chromosome.chromatids:
            chromatid.separate()

def telophase(cell):
    for chromosome in cell.chromosomes:
        chromosome.position = 'opposite poles'
    for nuclear_membrane in cell.nuclear_membranes:
        nuclear_membrane.position = 'opposite poles'
    for cell_membrane in cell.cell_membranes:
        cell_membrane.position = 'pinch'

def divide(cell):
    new_cell = Cell()
    new_cell.chromosomes = cell.chromosomes
    new_cell.centrioles = cell.centrioles
    new_cell.nuclear_membranes = cell.nuclear_membranes
    new_cell.cell_membranes = cell.cell_membranes
    return new_cell

cell = Cell()
prophase(cell)
centrioles_separation(cell)
metaphase(cell)
anaphase(cell)
telophase(cell)
new_cell = divide(cell)