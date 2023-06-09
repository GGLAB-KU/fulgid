class Volcano:
    def __init__(self):
        self.magma = Magma()

class Magma:
    def __init__(self):
        self.igneous_rock = IgneousRock()

class IgneousRock:
    def __init__(self):
        self.sediment = Sediment()

class Sediment:
    def __init__(self):
        self.sedimentary_rock = SedimentaryRock()

class SedimentaryRock:
    def __init__(self):
        self.metamorphic_rock = MetamorphicRock()

class MetamorphicRock:
    def __init__(self):
        self.heat_and_pressure = HeatAndPressure()

class HeatAndPressure:
    def __init__(self):
        self.magma = Magma()