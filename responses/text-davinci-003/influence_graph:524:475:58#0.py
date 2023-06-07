class Fetus:
    def __init__(self):
        self.stage = "fetus"

class Baby:
    def __init__(self, fetus):
        self.stage = "baby"
        self.fetus = fetus

class Child:
    def __init__(self, baby):
        self.stage = "child"
        self.baby = baby

class Adolescent:
    def __init__(self, child):
        self.stage = "adolescent"
        self.child = child

class Adult:
    def __init__(self, adolescent):
        self.stage = "adult"
        self.adolescent = adolescent

class Elderly:
    def __init__(self, adult):
        self.stage = "elderly"
        self.adult = adult

class Dead:
    def __init__(self, elderly):
        self.stage = "dead"
        self.elderly = elderly

fetus = Fetus()
baby = Baby(fetus)
child = Child(baby)
adolescent = Adolescent(child)
adult = Adult(adolescent)
elderly = Elderly(adult)
dead = Dead(elderly)