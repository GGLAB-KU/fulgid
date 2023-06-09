class Battery:
    def __init__(self):
        self.voltage = 0

class Flashlight:
    def __init__(self):
        self.batteries = []
        self.lamp = None
        self.reflector = None
        self.is_on = False
    
    def add_batteries(self, batteries):
        self.batteries = batteries
    
    def add_lamp(self, lamp):
        self.lamp = lamp
    
    def add_reflector(self, reflector):
        self.reflector = reflector
    
    def turn_on(self):
        self.is_on = True
        self.lamp.complete_circuit(self.batteries)
        self.lamp.glow()
        self.reflector.direct_beam()
    
    def turn_off(self):
        self.is_on = False
        self.lamp.break_circuit()
        self.lamp.stop_glowing()
        self.reflector.stop_directing_beam()

class Lamp:
    def __init__(self):
        self.is_glowing = False
    
    def complete_circuit(self, batteries):
        self.voltage = 0
        for battery in batteries:
            self.voltage += battery.voltage
    
    def break_circuit(self):
        self.voltage = 0
    
    def glow(self):
        self.is_glowing = True
    
    def stop_glowing(self):
        self.is_glowing = False

class Reflector:
    def __init__(self):
        self.is_directing_beam = False
    
    def direct_beam(self):
        self.is_directing_beam = True
    
    def stop_directing_beam(self):
        self.is_directing_beam = False