class PhotovoltaicCell:
    def __init__(self):
        self.top_layer = None
        self.bottom_layer = None
        self.electric_field = None
        self.sunlight = None
        self.electrons = None
        self.external_circuit = None
    
    def create_cell(self):
        self.top_layer = 'doped'
        self.bottom_layer = 'doped'
        self.electric_field = self.top_layer + self.bottom_layer
    
    def receive_sunlight(self):
        self.sunlight = True
        self.electrons = self.sunlight + self.electric_field
    
    def add_external_circuit(self):
        self.external_circuit = True
        self.electrons = self.electrons + self.external_circuit
    
    def provide_electricity(self):
        return self.electrons

class Owner:
    def __init__(self):
        self.cell = PhotovoltaicCell()
    
    def create_cell(self):
        self.cell.create_cell()
    
    def receive_sunlight(self):
        self.cell.receive_sunlight()
    
    def add_external_circuit(self):
        self.cell.add_external_circuit()
    
    def get_electricity(self):
        return self.cell.provide_electricity()