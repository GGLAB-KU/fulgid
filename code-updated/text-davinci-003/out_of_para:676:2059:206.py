class Plant:
    def __init__(self):
        self.alive = True

class Sediment:
    def __init__(self):
        self.contains_plant = False

class Decay:
    def __init__(self):
        self.soft_parts_decay = True

class Minerals:
    def __init__(self):
        self.replace_hard_parts = True

class Rock:
    def __init__(self):
        self.formed_from_sediment = True

class Erosion:
    def __init__(self):
        self.erode_rock = True

class Fossil:
    def __init__(self):
        self.appears_on_surface = True

def event(larvae_food):
    plant = Plant()
    sediment = Sediment()
    decay = Decay()
    minerals = Minerals()
    rock = Rock()
    erosion = Erosion()
    fossil = Fossil()

    if plant.alive:
        plant.alive = False
        sediment.contains_plant = True

    if sediment.contains_plant:
        if larvae_food == 'enough':
            decay.soft_parts_decay = True
        else:
            decay.soft_parts_decay = False
        minerals.replace_hard_parts = True

    if minerals.replace_hard_parts:
        rock.formed_from_sediment = True

    if rock.formed_from_sediment:
        erosion.erode_rock = True

    if erosion.erode_rock:
        fossil.appears_on_surface = True

    if decay.soft_parts_decay:
        return 'more'
    else:
        return 'less'

print(event('enough')) # Output: more
print(event('not enough')) # Output: less