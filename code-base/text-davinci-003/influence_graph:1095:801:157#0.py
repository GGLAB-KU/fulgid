class Star:
    def __init__(self):
        self.hydrogen = True
        self.red_giant = False
        self.core = False
        self.gasses = False
        self.white_dwarf = False
    
    def burn_hydrogen(self):
        self.hydrogen = False
        self.red_giant = True
    
    def burn_red_giant(self):
        self.red_giant = False
        self.core = True
        self.gasses = True
    
    def collapse_core(self):
        self.core = False
        self.gasses = False
        self.white_dwarf = True

class Universe:
    def __init__(self):
        self.stars = []
    
    def add_star(self, star):
        self.stars.append(star)
    
    def burn_hydrogen(self):
        for star in self.stars:
            star.burn_hydrogen()
    
    def burn_red_giant(self):
        for star in self.stars:
            star.burn_red_giant()
    
    def collapse_core(self):
        for star in self.stars:
            star.collapse_core()

# Create a star
star = Star()

# Create a universe
universe = Universe()

# Add the star to the universe
universe.add_star(star)

# Burn the hydrogen in the star
universe.burn_hydrogen()

# Burn the red giant in the star
universe.burn_red_giant()

# Collapse the core of the star
universe.collapse_core()