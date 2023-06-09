Class Tray:
    def __init__(self, water_amount):
        self.water = Water(water_amount)

class Freezer:
    def __init__(self):
        self.tray = None
    
    def insert_tray(self, tray):
        self.tray = tray
    
    def freeze(self):
        self.tray.water.slow_down()
        self.tray.water.become_ice()

class Water:
    def __init__(self, amount):
        self.amount = amount
        self.state = "liquid"
    
    def slow_down(self):
        if self.amount < 500:
            self.state = "slowing down"
        else:
            self.state = "not slowing down"
    
    def become_ice(self):
        if self.amount < 500:
            self.state = "less ice"
        else:
            self.state = "more ice"

# Main
tray = Tray(400)
freezer = Freezer()
freezer.insert_tray(tray)
freezer.freeze()

if tray.water.state == "less ice":
    print("Less ice cubes are made.")
elif tray.water.state == "more ice":
    print("More ice cubes are made.")
else:
    print("No effect on ice cubes.")