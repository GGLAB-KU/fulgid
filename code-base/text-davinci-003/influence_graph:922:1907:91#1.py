class Magma:
    def __init__(self):
        self.melted = False
        self.pressure = 0
        self.energy = 0

    def melt(self):
        self.melted = True

    def build_pressure(self):
        self.pressure += 1

    def convert_energy(self):
        self.energy += 1

class Volcano:
    def __init__(self):
        self.magma_chambers = []
        self.explosive = False

    def add_magma_chamber(self, magma_chamber):
        self.magma_chambers.append(magma_chamber)

    def set_explosive(self, explosive):
        self.explosive = explosive

class MagmaChamber:
    def __init__(self):
        self.magma = Magma()

    def add_magma(self, magma):
        self.magma = magma

class Earthquake:
    def __init__(self):
        self.magnitude = 0

    def increase_magnitude(self):
        self.magnitude += 1

# Create the objects
magma = Magma()
volcano = Volcano()
magma_chamber = MagmaChamber()
earthquake = Earthquake()

# Magma is formed when rock melts inside the Earth's crust
magma.melt()

# Magma rises
# Collects inside magma chambers underneath a volcano
volcano.add_magma_chamber(magma_chamber)
magma_chamber.add_magma(magma)

# Pressure builds in the magma chambers as they fill
magma.build_pressure()

# Gain energy for eruption
magma.convert_energy()

# Some of the energy is converted into seismic activity (earthquakes)
earthquake.increase_magnitude()

# If the magma building in the volcano is thick and sticky it will trap gases
# Results in an explosive eruption when the pressure becomes too intense
if magma.pressure > 5:
    volcano.set_explosive(True)

# If the magma is thin and runs
# The magma results in a low-pressure, slow-moving flow of magma instead of a violent eruption
else:
    volcano.set_explosive(False)