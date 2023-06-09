class Metal:
    def __init__(self, material):
        self.material = material

class ElectricalSource:
    def __init__(self, type):
        self.type = type

class Wire:
    def __init__(self, metal):
        self.metal = metal

class MagneticField:
    def __init__(self, wire):
        self.wire = wire

class Event:
    def __init__(self, metal, electrical_source, wire, magnetic_field):
        self.metal = metal
        self.electrical_source = electrical_source
        self.wire = wire
        self.magnetic_field = magnetic_field

    def start_event(self):
        self.wire.metal = self.metal
        self.magnetic_field.wire = self.wire
        self.electrical_source.type.start()
        self.magnetic_field.wire.metal.magnetize()
        self.magnetic_field.turn_on()

    def stop_event(self):
        self.magnetic_field.turn_off()
        self.electrical_source.type.stop()