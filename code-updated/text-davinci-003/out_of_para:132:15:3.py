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
        if self.blocked:
            return "Windpipe is blocked, oxygen cannot be transported"
        else:
            self.oxygen = oxygen
    
    def block(self):
        self.blocked = True
    
    def unblock(self):
        self.blocked = False

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

# Test the code
if __name__ == "__main__":
    nose_or_mouth = NoseOrMouth()
    windpipe = Windpipe()
    lungs = Lungs()

    nose_or_mouth.breathe_in(20)
    windpipe.transport_oxygen(nose_or_mouth.oxygen)
    lungs.send_oxygen(windpipe.oxygen)
    lungs.expel_carbon_dioxide(15)
    windpipe.transport_oxygen(lungs.air_sacs.oxygen)

    # Suppose there is less of an appetite, how will it affect windpipe if it is blocked?
    windpipe.block()
    if nose_or_mouth.oxygen < 10:
        print("Less appetite, windpipe is blocked, oxygen cannot be transported")
    else:
        print("Less appetite, windpipe is blocked, but oxygen can still be transported")
    windpipe.unblock()