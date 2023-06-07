class Virus:
    def __init__(self):
        self.receptors = []
    
    def attach_receptor(self, receptor):
        self.receptors.append(receptor)
        
    def infect_cell(self, cell):
        for receptor in self.receptors:
            receptor.dock_to_cell(cell)
            receptor.enter_cell(cell)
            receptor.take_over_cell(cell)
            receptor.produce_copies(cell)
            
class Receptor:
    def __init__(self):
        pass
    
    def dock_to_cell(self, cell):
        pass
    
    def enter_cell(self, cell):
        pass
    
    def take_over_cell(self, cell):
        pass
    
    def produce_copies(self, cell):
        pass
        
class Cell:
    def __init__(self):
        pass
    
    def accept_virus(self, virus):
        virus.infect_cell(self)
        
    def produce_copies(self):
        pass
    
    def release_copies(self):
        pass