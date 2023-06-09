class SolarRadiation:
    def __init__(self):
        self.energy = 0
    
    def reach_atmosphere(self):
        self.energy = self.energy + 1

class Atmosphere:
    def __init__(self):
        self.reflected_energy = 0
        self.absorbed_energy = 0
    
    def reflect_energy(self):
        self.reflected_energy = self.reflected_energy + 1
    
    def absorb_energy(self):
        self.absorbed_energy = self.absorbed_energy + 1

class Earth:
    def __init__(self):
        self.heat = 0
    
    def absorb_energy(self, energy):
        self.heat = self.heat + energy
    
    def radiate_heat(self):
        self.heat = self.heat - 1

class GreenhouseGases:
    def __init__(self):
        self.trapped_heat = 0
    
    def trap_heat(self, heat):
        self.trapped_heat = self.trapped_heat + heat

class HumanActivities:
    def __init__(self):
        self.emissions = 0
    
    def increase_emissions(self):
        self.emissions = self.emissions + 1

def main():
    # Create objects
    solar_radiation = SolarRadiation()
    atmosphere = Atmosphere()
    earth = Earth()
    greenhouse_gases = GreenhouseGases()
    human_activities = HumanActivities()

    # Solar radiation reaches Earth's atmosphere
    solar_radiation.reach_atmosphere()

    # Some is reflected back into space
    atmosphere.reflect_energy()

    # The rest of the energy is absorbed by land and oceans, heating the Earth
    atmosphere.absorb_energy()
    earth.absorb_energy(atmosphere.absorbed_energy)

    # Heat radiates from Earth to space
    earth.radiate_heat()

    # Some of this heat is trapped by greenhouse gases in the atmosphere
    greenhouse_gases.trap_heat(earth.heat)

    # Human activities such as burning fuel are increasing the amount of greenhouses gases
    human_activities.increase_emissions()

    # This causes more heat radiation to stay trapped in our atmosphere
    greenhouse_gases.trap_heat(human_activities.emissions)

    # The Earth's temperature rises
    earth.heat = earth.heat + greenhouse_gases.trapped_heat

if __name__ == '__main__':
    main()