class Larva:
    def __init__(self):
        self.born = True

class Caterpillar:
    def __init__(self, larva):
        self.larva = larva
        self.eat = True
        self.grow = True

class Cocoon:
    def __init__(self, caterpillar):
        self.caterpillar = caterpillar
        self.form = True

class Pupa:
    def __init__(self, cocoon):
        self.cocoon = cocoon
        self.transform = True

class Butterfly:
    def __init__(self, pupa):
        self.pupa = pupa
        self.hatch = True