import random

class Tree:
    def __init__(self, location):
        self.location = location
        self.seed_count = random.randint(50, 200)  # assuming a tree can produce between 50 to 200 seeds

    def produce_seeds(self):
        return [Seed(self) for _ in range(self.seed_count)]

class Seed:
    def __init__(self, parent_tree):
        self.parent_tree = parent_tree

    def get_dispersed(self):
        # For simplicity, we'll simulate dispersion by moving the seed to a random location near the parent tree
        dispersion_distance = random.uniform(0, 10)  # seeds can get dispersed up to 10 units away
        self.location = self.parent_tree.location + dispersion_distance
        return self.location

class Ground:
    def __init__(self):
        self.trees = []
        self.seeds = []

    def accept_seeds(self, seeds):
        for seed in seeds:
            seed.get_dispersed()
            self.seeds.append(seed)

    def grow_trees(self):
        for seed in self.seeds:
            self.trees.append(Tree(seed.location))
        self.seeds = []  # remove all seeds after they've grown into trees

def simulate_one_generation(ground):
    # Trees produce seeds
    for tree in ground.trees:
        seeds = tree.produce_seeds()
        ground.accept_seeds(seeds)

    # Seeds grow into new trees
    ground.grow_trees()


# Simulation
ground = Ground()

# Let's start with one tree
ground.trees.append(Tree(0))

# Now let's simulate this process for a few generations
for _ in range(10):
    simulate_one_generation(ground)
    print(f"After this generation, we have {len(ground.trees)} trees.")
