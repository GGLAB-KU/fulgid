class Kidney:
    def __init__(self):
        self.renal_artery = RenalArtery()
        self.nephrons = Nephrons()
        self.ureters = Ureters()

class RenalArtery:
    def __init__(self):
        self.blood = Blood()

class Nephrons:
    def __init__(self):
        self.blood = Blood()
        self.waste = Waste()
        self.water = Water()

class Ureters:
    def __init__(self):
        self.urine = Urine()

class Blood:
    pass

class Waste:
    pass

class Water:
    pass

class Urine:
    pass