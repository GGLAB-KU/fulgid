class CoffeePot:
    def __init__(self):
        self.water = None
        self.filter = None
        self.ground_coffee = None
        self.hot_water = None
        self.coffee = None
        
    def fill_water(self):
        self.water = True
        
    def pour_water(self):
        self.water = False
        self.hot_water = True
        
    def place_filter(self):
        self.filter = True
        
    def measure_coffee(self):
        self.ground_coffee = True
        
    def heat_water(self):
        self.hot_water = True
        
    def drip_coffee(self):
        self.coffee = True
        
class Machine:
    def __init__(self):
        self.well = None
        self.basket = None
        
    def fill_well(self, water):
        self.well = water
        
    def place_basket(self, filter):
        self.basket = filter
        
    def start_heating(self):
        self.hot_water = True
        
    def drip_coffee(self, ground_coffee):
        self.coffee = ground_coffee
        

def main():
    # create coffee pot and machine
    pot = CoffeePot()
    machine = Machine()
    
    # fill coffee pot with water
    pot.fill_water()
    
    # pour water into machine's well
    pot.pour_water()
    machine.fill_well(pot.water)
    
    # place filter in machine's basket
    pot.place_filter()
    machine.place_basket(pot.filter)
    
    # measure ground coffee into filter
    pot.measure_coffee()
    
    # turn on machine to start heating water
    machine.start_heating()
    
    # hot water rises up and drops into ground coffee
    pot.heat_water()
    
    # hot water passes through grounds and coffee drips into pot from basket
    machine.drip_coffee(pot.ground_coffee)
    pot.drip_coffee()
    
if __name__ == '__main__':
    main()