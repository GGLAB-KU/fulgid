class Butterfly:
    def __init__(self):
        self.egg = None
        self.cocoon = None
        self.mate = None
    
    def layEgg(self):
        self.egg = Egg()
    
    def spinCocoon(self):
        self.cocoon = Cocoon()
    
    def mate(self, other):
        self.mate = other
        other.mate = self
    
    def layEggs(self):
        self.egg = Egg()

class Egg:
    def __init__(self):
        self.larvae = Larvae()
    
    def hatch(self):
        return Caterpillar()

class Larvae:
    def __init__(self):
        self.caterpillar = None
    
    def mature(self):
        self.caterpillar = Caterpillar()

class Caterpillar:
    def __init__(self):
        self.cocoon = None
    
    def eat(self):
        pass
    
    def spinCocoon(self):
        self.cocoon = Cocoon()

class Cocoon:
    def __init__(self):
        self.pupa = Pupa()
    
    def formButterfly(self):
        return Butterfly()

class Pupa:
    def __init__(self):
        pass
    
    def formButterfly(self):
        return Butterfly()