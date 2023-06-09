class Host:
    def __init__(self):
        self.cells = []
 
    def addCell(self, cell):
        self.cells.append(cell)
 
    def getSick(self):
        for cell in self.cells:
            if cell.isInfected():
                self.sick = True
 
class Cell:
    def __init__(self):
        self.virus = None
 
    def isInfected(self):
        return self.virus != None
 
    def setVirus(self, virus):
        self.virus = virus
 
class Virus:
    def __init__(self):
        self.receptors = []
 
    def attachReceptor(self, receptor):
        self.receptors.append(receptor)
 
    def enterCell(self, cell):
        for receptor in self.receptors:
            if receptor.isCompatible(cell):
                cell.setVirus(self)
 
    def replicate(self, cell):
        newVirus = Virus()
        newVirus.attachReceptor(Receptor())
        newVirus.enterCell(cell)
 
class Receptor:
    def __init__(self):
        self.compatibleCells = []
 
    def isCompatible(self, cell):
        return cell in self.compatibleCells
 
host = Host()
cell1 = Cell()
cell2 = Cell()
host.addCell(cell1)
host.addCell(cell2)
virus = Virus()
virus.attachReceptor(Receptor())
virus.enterCell(cell1)
virus.replicate(cell2)
host.getSick()