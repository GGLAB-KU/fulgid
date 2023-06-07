class Tree:
    def __init__(self):
        self.seeds = []
    
    def produce_seeds(self):
        self.seeds.append(Seed())
        
class Seed:
    def __init__(self):
        self.dispersed = False
    
    def disperse(self):
        self.dispersed = True

class Wind:
    def __init__(self):
        self.seeds = []
    
    def pick_up_seeds(self, tree):
        self.seeds.extend(tree.seeds)
        tree.seeds = []
    
    def disperse_seeds(self):
        for seed in self.seeds:
            seed.disperse()

class Animal:
    def __init__(self):
        self.seeds = []
    
    def pick_up_seeds(self, tree):
        self.seeds.extend(tree.seeds)
        tree.seeds = []
    
    def disperse_seeds(self):
        for seed in self.seeds:
            seed.disperse()

class Ground:
    def __init__(self):
        self.seeds = []
    
    def receive_seeds(self, wind, animal):
        self.seeds.extend(wind.seeds)
        self.seeds.extend(animal.seeds)
        wind.seeds = []
        animal.seeds = []
    
    def grow_trees(self):
        for seed in self.seeds:
            new_tree = Tree()
            new_tree.produce_seeds()

# Main
tree = Tree()
tree.produce_seeds()

wind = Wind()
animal = Animal()

wind.pick_up_seeds(tree)
animal.pick_up_seeds(tree)

wind.disperse_seeds()
animal.disperse_seeds()

ground = Ground()
ground.receive_seeds(wind, animal)
ground.grow_trees()