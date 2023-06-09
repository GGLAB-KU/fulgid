class Tree:
    def __init__(self, nutrients, is_dead=False):
        self.nutrients = nutrients
        self.is_dead = is_dead

    def die_off(self):
        self.is_dead = True
        self.nutrients = 0

    def provide_nutrients(self):
        if self.is_dead:
            return self.nutrients * 2
        else:
            return self.nutrients

class Forest:
    def __init__(self, trees):
        self.trees = trees

    def form_networks(self):
        for tree in self.trees:
            tree.connect_to_other_trees()

    def get_dead_tree_count(self):
        count = 0
        for tree in self.trees:
            if tree.is_dead:
                count += 1
        return count

class Organism:
    def __init__(self, shelter):
        self.shelter = shelter

    def thrive(self):
        self.shelter.provide_shelter()

class Shadow:
    def __init__(self, intensity):
        self.intensity = intensity

    def affect_forest(self, forest):
        dead_tree_count = forest.get_dead_tree_count()
        if dead_tree_count == 0:
            return 'no effect'
        elif dead_tree_count < 5:
            return 'less'
        else:
            return 'more'

def create_forest():
    trees = []
    for i in range(10):
        trees.append(Tree(10))
    forest = Forest(trees)
    forest.form_networks()
    for tree in forest.trees:
        tree.die_off()
    for tree in forest.trees:
        tree.provide_nutrients()
    for tree in forest.trees:
        organism = Organism(tree)
        organism.thrive()
    return forest

forest = create_forest()
shadow = Shadow(10)
effect = shadow.affect_forest(forest)
print(effect)