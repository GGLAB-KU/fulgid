class MiningOperation:
    def __init__(self):
        self.oil = 0

    def gather_oil(self, amount):
        self.oil += amount

class Store:
    def __init__(self):
        self.oil = 0

    def receive_oil(self, oil):
        self.oil += oil

class Homeowner:
    def __init__(self):
        self.oil = 0

    def purchase_oil(self, store, amount):
        if store.oil >= amount:
            self.oil += amount
            store.oil -= amount
        else:
            self.oil += store.oil
            store.oil = 0

class Stove:
    def __init__(self):
        self.oil = 0

    def place_oil(self, homeowner, amount):
        if homeowner.oil >= amount:
            self.oil += amount
            homeowner.oil -= amount
        else:
            self.oil += homeowner.oil
            homeowner.oil = 0

    def light_oil(self):
        if self.oil > 0:
            self.oil -= 1

class House:
    def __init__(self):
        self.warm_air = 0

    def receive_warm_air(self, stove):
        self.warm_air += stove.oil
        stove.oil = 0

# Create objects
mining_operation = MiningOperation()
store = Store()
homeowner = Homeowner()
stove = Stove()
house = House()

# Gather oil
mining_operation.gather_oil(1)

# Transport oil
store.receive_oil(mining_operation.oil)

# Purchase oil
homeowner.purchase_oil(store, 5)

# Place oil
stove.place_oil(homeowner, 3)

# Light oil
stove.light_oil()

# Receive warm air
house.receive_warm_air(stove)

# Answer the question
if mining_operation.oil < 1:
    print("less")
    if homeowner.oil > 0:
        print("more")
    else:
        print("no effect")
else:
    print("no effect")