
class Bird:
    def __init__(self):
        self.tree = None
        self.twigs = []
        self.refuse = []
        self.nest = None
    
    def pick_tree(self, tree):
        self.tree = tree
    
    def collect_twigs(self, twigs):
        self.twigs.extend(twigs)
    
    def collect_refuse(self, refuse):
        self.refuse.extend(refuse)
    
    def make_base(self):
        self.nest = Nest(self.twigs)
    
    def make_sides(self):
        self.nest.add_sides(self.twigs, self.refuse)
    
    def add_soft_material(self):
        self.nest.add_soft_material()

class Tree:
    def __init__(self):
        self.twigs = []
        self.refuse = []
    
    def get_twigs(self):
        return self.twigs
    
    def get_refuse(self):
        return self.refuse

class Nest:
    def __init__(self, twigs):
        self.base = twigs
        self.sides = []
        self.soft_material = []
    
    def add_sides(self, twigs, refuse):
        self.sides.extend(twigs + refuse)
    
    def add_soft_material(self):
        self.soft_material.extend(self.sides)
    
    def get_size(self):
        return len(self.base) + len(self.sides) + len(self.soft_material)

    def weather_effect(self, weather):
        if weather == 'bad':
            return 'more' if self.get_size() > 10 else 'less'
        else:
            return 'no effect'

# Example usage
bird = Bird()
tree = Tree()
tree.twigs = [1, 2, 3, 4, 5]
tree.refuse = ['leaves', 'grass']
bird.pick_tree(tree)
bird.collect_twigs([6, 7, 8])
bird.collect_refuse(['feathers'])
bird.make_base()
bird.make_sides()
bird.add_soft_material()
nest_size = bird.nest.get_size()
weather = 'bad'
weather_effect = bird.nest.weather_effect(weather)
print(f"The nest size is {nest_size} and the weather effect is {weather_effect}.")