class Participant:
    def __init__(self):
        self.oxygen = None
        self.carbon_dioxide = None

class NoseOrMouth(Participant):
    def __init__(self):
        super().__init__()
    
    def breathe_in(self, oxygen):
        self.oxygen = oxygen

class Windpipe(Participant):
    def __init__(self):
        super().__init__()
    
    def transport_oxygen(self, oxygen):
        self.oxygen = oxygen

class Lungs(Participant):
    def __init__(self):
        super().__init__()
        self.air_sacs = AirSacs()
    
    def send_oxygen(self, oxygen):
        self.air_sacs.receive_oxygen(oxygen)
    
    def expel_carbon_dioxide(self, carbon_dioxide):
        self.carbon_dioxide = carbon_dioxide

class AirSacs(Participant):
    def __init__(self):
        super().__init__()
    
    def receive_oxygen(self, oxygen):
        self.oxygen = oxygen
    
    def transfer_carbon_dioxide(self, carbon_dioxide):
        self.carbon_dioxide = carbon_dioxide