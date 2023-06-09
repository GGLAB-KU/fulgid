class Wood:
    def __init__(self, finish):
        self.finish = finish
    
    def get_finish(self):
        return self.finish
    
    def lose_luster(self):
        self.finish = None

class Rain:
    def __init__(self):
        pass
    
    def seep_into_wood(self, wood):
        wood.lose_luster()
    
    def evaporate(self, wood, water_amount):
        if water_amount > 10:
            return "more"
        else:
            wood.get_finish()
            return "no effect"
    
    def take_finish_with_it(self, wood):
        wood.finish = None

wood = Wood("paint")
rain = Rain()

rain.seep_into_wood(wood)
water_amount = 15
effect = rain.evaporate(wood, water_amount)
rain.take_finish_with_it(wood)

print(effect)