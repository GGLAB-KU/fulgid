class Sun:
    def __init__(self):
        self.mass = 0
        self.pressure = 0

class HydrogenAtom:
    def __init__(self):
        self.fused = False

class NuclearReaction:
    def __init__(self):
        self.energy = 0

class Light:
    def __init__(self):
        self.traveled = False

class Earth:
    def __init__(self):
        self.receivedLight = False

def main():
    sun = Sun()
    sun.mass = 50  # less mass pulled
    sun.pressure = 1000

    atoms = []
    for i in range(100):
        atoms.append(HydrogenAtom())

    reaction = NuclearReaction()
    reaction.energy = 1000

    light = Light()
    if sun.mass < 100:  # less mass pulled
        light.traveled = False  # less light to travel
    else:
        light.traveled = True

    earth = Earth()
    earth.receivedLight = True

    if light.traveled:
        print("The light traveled to Earth.")
    else:
        print("Less light traveled to Earth.")

if __name__ == "__main__":
    main()