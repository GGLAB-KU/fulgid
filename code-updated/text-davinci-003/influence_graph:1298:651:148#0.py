class Kidney:
    def __init__(self, water_level):
        self.renal_artery = RenalArtery()
        self.nephrons = Nephrons(water_level)
        self.ureters = Ureters()

class RenalArtery:
    def __init__(self):
        self.blood = Blood()

class Nephrons:
    def __init__(self, water_level):
        self.blood = Blood()
        self.waste = Waste()
        self.water = Water(water_level)

    def filter(self):
        if self.water.level == 'low':
            return 'less'
        else:
            return 'more'

class Ureters:
    def __init__(self):
        self.urine = Urine()

class Blood:
    pass

class Waste:
    pass

class Water:
    def __init__(self, level):
        self.level = level

class Urine:
    pass

water_level = 'low'
kidney = Kidney(water_level)
waste_removal = kidney.nephrons.filter()
print(waste_removal) # Output: less