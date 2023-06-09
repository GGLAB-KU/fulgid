Class Bird:
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

Class Tree:
    def __init__(self):
        self.twigs = []
        self.refuse = []
    
    def get_twigs(self):
        return self.twigs
    
    def get_refuse(self):
        return self.refuse

Class Nest:
    def __init__(self, twigs):
        self.base = twigs
        self.sides = []
        self.soft_material = []
    
    def add_sides(self, twigs, refuse):
        self.sides.extend(twigs + refuse)
    
    def add_soft_material(self):
        self.soft_material.extend(self.sides)