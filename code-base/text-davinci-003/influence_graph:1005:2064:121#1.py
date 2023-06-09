Class Tray:
    def __init__(self):
        self.water = None

Class Freezer:
    def __init__(self):
        self.tray = None
    
    def insert_tray(self, tray):
        self.tray = tray
    
    def freeze(self):
        self.tray.water.slow_down()
        self.tray.water.become_ice()

Class Water:
    def __init__(self):
        self.state = "liquid"
    
    def slow_down(self):
        self.state = "slowing down"
    
    def become_ice(self):
        self.state = "ice"

# Main
tray = Tray()
tray.water = Water()

freezer = Freezer()
freezer.insert_tray(tray)
freezer.freeze()

print("The ice cubes are ready.")