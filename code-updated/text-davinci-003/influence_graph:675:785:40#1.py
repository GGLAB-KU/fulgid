class Animal:
    def __init__(self):
        self.alive = True

class Plant:
    def __init__(self):
        self.alive = True

class Soil:
    def __init__(self):
        self.soft = True

class Sediment:
    def __init__(self):
        self.builds_up = True

class Decomposition:
    def __init__(self):
        self.remains = True

class TraceAmounts:
    def __init__(self):
        self.left = True

class Mineral:
    def __init__(self):
        self.replacement = True

class Fossil:
    def __init__(self):
        self.formed = True

def event(flood):
    animal = Animal()
    plant = Plant()
    soil = Soil()
    sediment = Sediment()
    decomposition = Decomposition()
    trace_amounts = TraceAmounts()
    mineral = Mineral()
    fossil = Fossil()

    if flood:
        return 'less'
    elif animal.alive and plant.alive and soil.soft:
        sediment.builds_up
        decomposition.remains
        trace_amounts.left
        mineral.replacement
        fossil.formed
        return 'more'
    else:
        return 'no effect'

print(event(True)) # less