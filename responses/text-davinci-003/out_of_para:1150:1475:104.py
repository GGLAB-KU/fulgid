class PhotovoltaicCell:
    def __init__(self):
        self.top_layer = None
        self.bottom_layer = None
        self.electric_field = None
        self.sunlight = None
        self.electrons = None
        self.external_circuit = None
    
    def create_cell(self):
        self.top_layer = SemiconductorMaterial('negative')
        self.bottom_layer = SemiconductorMaterial('positive')
        self.electric_field = ElectricField(self.top_layer, self.bottom_layer)
    
    def receive_sunlight(self):
        self.sunlight = Sunlight()
        self.electrons = self.sunlight.knock_electrons_loose(self.electric_field)
    
    def add_external_circuit(self):
        self.external_circuit = ExternalCircuit()
        self.external_circuit.allow_exchange(self.electrons)
    
    def give_electricity(self):
        self.owner.receive_electricity(self.external_circuit)

class SemiconductorMaterial:
    def __init__(self, charge):
        self.charge = charge

class ElectricField:
    def __init__(self, top_layer, bottom_layer):
        self.top_layer = top_layer
        self.bottom_layer = bottom_layer

class Sunlight:
    def __init__(self):
        pass
    
    def knock_electrons_loose(self, electric_field):
        return electric_field.top_layer.charge + electric_field.bottom_layer.charge

class ExternalCircuit:
    def __init__(self):
        pass
    
    def allow_exchange(self, electrons):
        pass

class Owner:
    def __init__(self):
        pass
    
    def receive_electricity(self, external_circuit):
        pass