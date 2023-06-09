class Earth:
    def __init__(self):
        self.crust = []
        self.plates = []

class Magma:
    def __init__(self):
        self.pressure = 0

class Plate:
    def __init__(self):
        self.movement = 0

class Eruption:
    def __init__(self):
        self.lava = []

class Lava:
    def __init__(self):
        self.cooling = 0

class Volcano:
    def __init__(self):
        self.rock = []

#Relationships
earth = Earth()
magma = Magma()
plate = Plate()
eruption = Eruption()
lava = Lava()
volcano = Volcano()

#Steps
#1 Magma rises through cracks in the Earth's crust
earth.crust.append(magma)

#2 The pressure causes plates to move
magma.pressure += 1
plate.movement += 1

#3 Magma explodes to the surface
eruption.lava.append(magma)

#4 The lava from the eruption cools to form new crust
lava.cooling += 1
earth.crust.append(lava)

#5 After several eruptions, the rock builds up and a volcano forms
for i in range(0,several):
    eruption.lava.append(lava)
    volcano.rock.append(lava)