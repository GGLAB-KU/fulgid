class Host:
    def __init__(self):
        self.cells = []
        self.sick = False
 
    def get_sick(self):
        for cell in self.cells:
            if cell.is_infected():
                self.sick = True
 
    def get_illness_severity(self):
        if len(self.cells) < 100:
            return 'less'
        elif len(self.cells) > 1000:
            return 'more'
        else:
            return 'no effect'
 
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
 
# Testing the code
host = Host()
for i in range(500):
    host.cells.append(Cell())
 
virus = Virus()
for i in range(10):
    virus.receptors.append(Receptor())
 
for cell in host.cells[:50]:
    virus.attach_to_cell(cell)
 
for i in range(10):
    new_virus = virus.replicate()
    for receptor in virus.receptors:
        new_receptor = Receptor()
        new_receptor.target_cell = receptor.target_cell
        new_virus.receptors.append(new_receptor)
    virus = new_virus
 
host.get_sick()
illness_severity = host.get_illness_severity()
print("If fewer cells are entered, the person will be", illness_severity, "ill.")