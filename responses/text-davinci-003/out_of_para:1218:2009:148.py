class Tree:
    def __init__(self):
        self.alive = True
    
    def die(self):
        self.alive = False

class Forest:
    def __init__(self):
        self.trees = []
    
    def add_tree(self, tree):
        self.trees.append(tree)
    
    def remove_tree(self, tree):
        self.trees.remove(tree)

class Organism:
    def __init__(self):
        self.shelter = None
    
    def find_shelter(self, tree):
        self.shelter = tree

def create_forest():
    forest = Forest()
    for _ in range(10):
        tree = Tree()
        forest.add_tree(tree)
    return forest

def simulate_forest_cycle(forest):
    for tree in forest.trees:
        tree.die()
        organism = Organism()
        organism.find_shelter(tree)
        forest.remove_tree(tree)
        new_tree = Tree()
        forest.add_tree(new_tree)

forest = create_forest()
simulate_forest_cycle(forest)