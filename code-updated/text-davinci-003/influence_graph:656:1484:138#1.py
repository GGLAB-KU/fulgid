class Larva:
    def __init__(self):
        self.born = True

class Caterpillar:
    def __init__(self, larva):
        self.larva = larva
        self.eat = True
        self.grow = True

class Cocoon:
    def __init__(self, caterpillar, pollution):
        self.caterpillar = caterpillar
        self.form = True
        if pollution == 'more':
            self.hatch_time = 10
        elif pollution == 'less':
            self.hatch_time = 20
        else:
            self.hatch_time = 15

class Pupa:
    def __init__(self, cocoon):
        self.cocoon = cocoon
        self.transform = True

class Butterfly:
    def __init__(self, pupa):
        self.pupa = pupa
        self.hatch = True

larva = Larva()
caterpillar = Caterpillar(larva)
cocoon = Cocoon(caterpillar, 'more')
pupa = Pupa(cocoon)
butterfly = Butterfly(pupa)

print("If there is more pollution, it will have a 'more' effect on cocoon hatches.")