class Man:
    def __init__(self):
        self.mating = False

class Woman:
    def __init__(self):
        self.mating = False

class Embryo:
    def __init__(self, man, woman):
        self.man = man
        self.woman = woman
        self.development_stage = 0

class Fetus:
    def __init__(self, embryo):
        self.embryo = embryo
        self.development_stage = 1

class Infant:
    def __init__(self, fetus):
        self.fetus = fetus
        self.development_stage = 2

class Child:
    def __init__(self, infant):
        self.infant = infant
        self.development_stage = 3

class Teenager:
    def __init__(self, child):
        self.child = child
        self.development_stage = 4

class Adult:
    def __init__(self, teenager):
        self.teenager = teenager
        self.development_stage = 5
        self.mating = True

def mate(man, woman):
    man.mating = True
    woman.mating = True
    return Embryo(man, woman)

def grow(embryo):
    if embryo.development_stage == 0:
        return Fetus(embryo)
    elif embryo.development_stage == 1:
        return Infant(embryo)
    elif embryo.development_stage == 2:
        return Child(embryo)
    elif embryo.development_stage == 3:
        return Teenager(embryo)
    elif embryo.development_stage == 4:
        return Adult(embryo)

def procreate(adult, wombs_available):
    if adult.mating and wombs_available > 0:
        man = Man()
        woman = Woman()
        return mate(man, woman), wombs_available - 1
    else:
        return None, wombs_available

def simulate_births(num_wombs):
    man = Man()
    woman = Woman()
    embryo = mate(man, woman)
    fetus = grow(embryo)
    infant = grow(fetus)
    child = grow(infant)
    teenager = grow(child)
    adult = grow(teenager)
    num_babies = 1
    for i in range(18, 50):
        embryo, num_wombs = procreate(adult, num_wombs)
        if embryo:
            num_babies += 1
            fetus = grow(embryo)
            infant = grow(fetus)
            child = grow(infant)
            teenager = grow(child)
            adult = grow(teenager)
        else:
            adult.mating = False
    return num_babies

# Testing the function with different number of wombs available
print("If there are more wombs available, the number of babies will be:", simulate_births(10))
print("If there are less wombs available, the number of babies will be:", simulate_births(5))
print("If there are no wombs available, the number of babies will be:", simulate_births(0))