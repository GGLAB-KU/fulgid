class Sunlight:
    def __init__(self):
        self.intensity = 0

class Greenhouse:
    def __init__(self):
        self.glass = Glass()
        self.plants = Plants()
        self.floor = Floor()
        self.air = Air()

class Glass:
    def __init__(self):
        self.transparency = 0

class Plants:
    def __init__(self):
        self.absorption = 0

class Floor:
    def __init__(self):
        self.absorption = 0

class Air:
    def __init__(self):
        self.carbon_dioxide = True

def main():
    sunlight = Sunlight()
    greenhouse = Greenhouse()

    # Sunlight passes through the glass into the greenhouse
    sunlight.intensity = greenhouse.glass.transparency

    # The plants and floor absorb the the sunlight
    sunlight.intensity -= greenhouse.plants.absorption + greenhouse.floor.absorption

    # The absorbed sunlight is converted to heat
    heat = sunlight.intensity

    # The heat cannot escape the glass
    heat = heat * greenhouse.glass.transparency

    # The heat is trapped in the greenhouse
    trapped_heat = heat

    # The hot air rises
    hot_air = trapped_heat

    # The colder air at the top is pushed to the bottom
    cold_air = hot_air

    # The colder air is then warmed by the floor and the plants.
    cold_air += greenhouse.floor.absorption + greenhouse.plants.absorption

    # If air is cleared of carbon dioxide, the greenhouse will be COLDER
    if not greenhouse.air.carbon_dioxide:
        cold_air -= 1

    if cold_air > 0:
        print("The greenhouse is warmer.")
    elif cold_air < 0:
        print("The greenhouse is colder.")
    else:
        print("The greenhouse temperature has no effect.")

if __name__ == "__main__":
    main()