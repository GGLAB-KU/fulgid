class PhotovoltaicCell:
    def __init__(self):
        self.top_layer = None
        self.bottom_layer = None
        self.electric_field = None
        self.sunlight = None
        self.electrons = None
        self.external_circuit = None
    
    def create_cell(self):
        self.top_layer = 'doped'
        self.bottom_layer = 'doped'
        self.electric_field = self.top_layer + self.bottom_layer
    
    def receive_sunlight(self, sunlight):
        self.sunlight = sunlight
        self.electrons = self.sunlight + self.electric_field
    
    def add_external_circuit(self):
        self.external_circuit = True
        self.electrons = self.electrons + self.external_circuit
    
    def provide_electricity(self):
        return self.electrons

class Owner:
    def __init__(self):
        self.cell = PhotovoltaicCell()
    
    def create_cell(self):
        self.cell.create_cell()
    
    def receive_sunlight(self, sunlight):
        self.cell.receive_sunlight(sunlight)
    
    def add_external_circuit(self):
        self.cell.add_external_circuit()
    
    def get_electricity(self):
        return self.cell.provide_electricity()

class SunnyDay:
    def __init__(self):
        self.sunlight = 'more'

class LessSunnyDay:
    def __init__(self):
        self.sunlight = 'less'

class NoSunnyDay:
    def __init__(self):
        self.sunlight = 'no effect'

owner = Owner()
owner.create_cell()

sunny_day = SunnyDay()
owner.receive_sunlight(sunny_day.sunlight)
owner.add_external_circuit()
electricity_on_sunny_day = owner.get_electricity()

less_sunny_day = LessSunnyDay()
owner.receive_sunlight(less_sunny_day.sunlight)
owner.add_external_circuit()
electricity_on_less_sunny_day = owner.get_electricity()

no_sunny_day = NoSunnyDay()
owner.receive_sunlight(no_sunny_day.sunlight)
owner.add_external_circuit()
electricity_on_no_sunny_day = owner.get_electricity()

if electricity_on_sunny_day > electricity_on_less_sunny_day:
    print('Less sunny days will have a negative effect on the amount of electricity produced.')
elif electricity_on_sunny_day < electricity_on_less_sunny_day:
    print('Less sunny days will have no effect on the amount of electricity produced.')
else:
    print('Less sunny days will have no effect on the amount of electricity produced.')