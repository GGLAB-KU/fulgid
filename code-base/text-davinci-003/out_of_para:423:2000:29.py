class Mine:
    def __init__(self, location):
        self.location = location

class Miners:
    def __init__(self, name):
        self.name = name
    
    def enter_mine(self, mine):
        self.mine = mine
    
    def remove_coal(self, mine):
        self.mine = mine

class Carts:
    def __init__(self):
        self.coal = []
    
    def add_coal(self, coal):
        self.coal.append(coal)

class ConveyorBelt:
    def __init__(self):
        self.coal = []
    
    def add_coal(self, coal):
        self.coal.append(coal)

class Truck:
    def __init__(self):
        self.coal = []
    
    def load_coal(self, coal):
        self.coal.append(coal)
    
    def take_coal(self, power_station):
        self.power_station = power_station

class PowerStation:
    def __init__(self, location):
        self.location = location
    
    def receive_coal(self, truck):
        self.truck = truck