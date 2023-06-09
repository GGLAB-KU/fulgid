class Cloud:
    def __init__(self):
        self.water_droplets = []
 
    def get_cold(self):
        for droplet in self.water_droplets:
            droplet.become_cold()
 
    def add_water_droplets(self, droplet):
        self.water_droplets.append(droplet)
 
 
class WaterDroplet:
    def __init__(self):
        self.temperature = 0
 
    def become_cold(self):
        self.temperature = -10
 
    def form_ice_crystal(self):
        return IceCrystal()
 
 
class IceCrystal:
    def __init__(self):
        self.size = 0
 
    def absorb_water_droplets(self, droplet):
        self.size += 1
 
    def form_snowflake(self):
        return Snowflake()
 
 
class Snowflake:
    def __init__(self):
        self.size = 0
 
    def fall_to_ground(self):
        pass
 
 
def main():
    cloud = Cloud()
    for _ in range(10):
        droplet = WaterDroplet()
        cloud.add_water_droplets(droplet)
 
    cloud.get_cold()
 
    for droplet in cloud.water_droplets:
        ice_crystal = droplet.form_ice_crystal()
        ice_crystal.absorb_water_droplets(droplet)
        snowflake = ice_crystal.form_snowflake()
        snowflake.fall_to_ground()
 
 
if __name__ == '__main__':
    main()