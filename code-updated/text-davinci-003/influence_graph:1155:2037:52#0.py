class Ocean:
    def __init__(self):
        self.bottom = []

class Mud:
    def __init__(self):
        self.bottom = []

class Sand:
    def __init__(self):
        self.bottom = []

class DeadOrganicMaterial:
    def __init__(self):
        self.bottom = []

class Kerogen:
    def __init__(self):
        self.molecules = []

class Petroleum:
    def __init__(self):
        self.molecules = []

class NaturalGas:
    def __init__(self):
        self.molecules = []

def accumulate(ocean, mud, sand, dead_organic_material):
    ocean.bottom.append(mud)
    ocean.bottom.append(sand)
    ocean.bottom.append(dead_organic_material)

def transform(ocean):
    kerogen = Kerogen()
    for item in ocean.bottom:
        if type(item) == DeadOrganicMaterial:
            kerogen.molecules.append(item)
    return kerogen

def crack(kerogen):
    petroleum = Petroleum()
    natural_gas = NaturalGas()
    for molecule in kerogen.molecules:
        if molecule.is_light():
            petroleum.molecules.append(molecule)
        else:
            natural_gas.molecules.append(molecule)
    return petroleum, natural_gas

def sediment_effect(sediment):
    if sediment == 'more':
        return 'less'
    elif sediment == 'less':
        return 'more'
    else:
        return 'no effect'

ocean = Ocean()
mud = Mud()
sand = Sand()
dead_organic_material = DeadOrganicMaterial()

accumulate(ocean, mud, sand, dead_organic_material)
kerogen = transform(ocean)
petroleum, natural_gas = crack(kerogen)

print("If more sediment forms, it will have a", sediment_effect('more'), "effect on the amount of oil.")