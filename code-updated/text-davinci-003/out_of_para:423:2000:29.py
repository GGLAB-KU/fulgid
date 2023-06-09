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

class Limestone:
    def __init__(self, location):
        self.location = location

class ConveyorBeltLimestone:
    def __init__(self):
        self.limestone = []
    
    def add_limestone(self, limestone):
        self.limestone.append(limestone)

class TruckLimestone:
    def __init__(self):
        self.limestone = []
    
    def load_limestone(self, limestone):
        self.limestone.append(limestone)
    
    def take_limestone(self, factory):
        self.factory = factory

class Factory:
    def __init__(self, location):
        self.location = location
    
    def receive_limestone(self, truck_limestone):
        self.truck_limestone = truck_limestone
    
    def produce_cement(self):
        self.cement = True

mine = Mine("Mountain A")
miners = Miners("John")
miners.enter_mine(mine)
carts = Carts()
conveyor_belt = ConveyorBelt()
truck = Truck()
power_station = PowerStation("City A")
limestone = Limestone("Mountain B")
conveyor_belt_limestone = ConveyorBeltLimestone()
truck_limestone = TruckLimestone()
factory = Factory("City B")

# Coal mining process
miners.remove_coal(mine)
carts.add_coal(miners.mine)
conveyor_belt.add_coal(carts.coal)
truck.load_coal(conveyor_belt.coal)
truck.take_coal(power_station)
power_station.receive_coal(truck)

# Limestone mining process
conveyor_belt_limestone.add_limestone(limestone)
truck_limestone.load_limestone(conveyor_belt_limestone.limestone)
truck_limestone.take_limestone(factory)
factory.receive_limestone(truck_limestone)

# Cement production process
factory.produce_cement()

# Answer to the question
print("If more limestone is excavated, it will have no effect on the arrival of coal at the power station.")