class Firebox:
    def __init__(self):
        self.coal = None

class Boiler:
    def __init__(self):
        self.pressure = None
        self.steam = None

class Cylinder:
    def __init__(self):
        self.steam = None

class Piston:
    def __init__(self):
        self.plunger = None

class Crank:
    def __init__(self):
        self.connecting_rod = None

class Wheels:
    def __init__(self):
        self.power = None

class OutletValve:
    def __init__(self):
        self.steam = None

class Chimney:
    def __init__(self):
        self.steam = None

def main():
    firebox = Firebox()
    firebox.coal = "coal"
    
    boiler = Boiler()
    boiler.pressure = "high pressure"
    boiler.steam = "steam"
    
    cylinder = Cylinder()
    cylinder.steam = boiler.steam
    
    piston = Piston()
    piston.plunger = "tight-fitting plunger"
    
    crank = Crank()
    crank.connecting_rod = "connecting rod"
    
    wheels = Wheels()
    wheels.power = "power the train along"
    
    outlet_valve = OutletValve()
    outlet_valve.steam = piston.steam
    
    chimney = Chimney()
    chimney.steam = outlet_valve.steam

if __name__ == "__main__":
    main()