class Leaf:
    def __init__(self):
        self.stomates = []
        self.xylem = []
        self.light_reaction = []
        self.atp = []
        self.sugar = []
        self.water_vapor = []

class CarbonDioxide:
    def __init__(self):
        self.diffusion = []

class Water:
    def __init__(self):
        self.transport = []

class Energy:
    def __init__(self):
        self.harvest = []

class Oxygen:
    def __init__(self):
        self.diffusion = []

def process(leaf, carbon_dioxide, water, energy, oxygen):
    # Carbon dioxide enters the leaves through the stomates by diffusion
    leaf.stomates.append(carbon_dioxide.diffusion)

    # Water is transported to the leaves in the xylem
    leaf.xylem.append(water.transport)

    # Energy harvested through light reaction is stored by forming ATP
    leaf.light_reaction.append(energy.harvest)
    leaf.atp.append(energy.harvest)

    # Carbon dioxide and energy from ATP are used to create sugar
    leaf.sugar.append(carbon_dioxide.diffusion)
    leaf.sugar.append(energy.harvest)

    # Oxygen exits the leaves through the stomata by diffusion
    leaf.stomates.append(oxygen.diffusion)

    # The plant reuses the water or the water exits through the stomata as water vapor.
    leaf.water_vapor.append(water.transport)

leaf = Leaf()
carbon_dioxide = CarbonDioxide()
water = Water()
energy = Energy()
oxygen = Oxygen()

process(leaf, carbon_dioxide, water, energy, oxygen)