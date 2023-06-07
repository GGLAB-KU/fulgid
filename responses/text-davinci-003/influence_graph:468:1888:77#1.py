class SaltWater:
    def __init__(self):
        self.heated = False
        self.gasified = False
        self.salt_particles = True

class Container:
    def __init__(self):
        self.salt_water = SaltWater()
        self.fresh_water = False

class HeatingProcess:
    def __init__(self, container):
        self.container = container
    
    def heat_salt_water(self):
        self.container.salt_water.heated = True
        self.container.salt_water.gasified = True
        self.container.salt_water.salt_particles = False

class PipingProcess:
    def __init__(self, container):
        self.container = container
    
    def pipe_gasified_water(self):
        self.container.fresh_water = True

class CoolingProcess:
    def __init__(self, container):
        self.container = container
    
    def cool_water(self):
        self.container.salt_water.gasified = False

# create container
container = Container()

# heat salt water
heating_process = HeatingProcess(container)
heating_process.heat_salt_water()

# pipe gasified water
piping_process = PipingProcess(container)
piping_process.pipe_gasified_water()

# cool water
cooling_process = CoolingProcess(container)
cooling_process.cool_water()