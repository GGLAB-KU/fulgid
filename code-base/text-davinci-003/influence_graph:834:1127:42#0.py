class Host:
    def __init__(self):
        self.cells = []
 
    def get_sick(self):
        for cell in self.cells:
            if cell.is_infected():
                self.sick = True
 
class Cell:
    def __init__(self):
        self.virus = None
 
    def is_infected(self):
        return self.virus != None
 
    def infect(self, virus):
        self.virus = virus
 
class Virus:
    def __init__(self):
        self.receptors = []
 
    def attach_to_cell(self, cell):
        for receptor in self.receptors:
            if receptor.can_attach_to(cell):
                cell.infect(self)
 
    def replicate(self):
        return Virus()
 
class Receptor:
    def __init__(self):
        self.target_cell = None
 
    def can_attach_to(self, cell):
        return self.target_cell == cell