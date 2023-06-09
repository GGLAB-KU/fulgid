class Sugar:
    def __init__(self):
        self.level = 0

class Bloodstream:
    def __init__(self):
        self.sugar_level = 0
    
    def add_sugar(self, sugar):
        self.sugar_level += sugar

class Pancreas:
    def __init__(self):
        self.insulin = 0
    
    def release_insulin(self):
        self.insulin += 1

class Body:
    def __init__(self):
        self.bloodstream = Bloodstream()
        self.pancreas = Pancreas()
    
    def add_sugar(self, sugar):
        self.bloodstream.add_sugar(sugar)
        self.pancreas.release_insulin()
    
    def lower_sugar_level(self):
        self.bloodstream.sugar_level -= self.pancreas.insulin

# Create sugar
sugar = Sugar()

# Create body
body = Body()

# Add sugar to body
body.add_sugar(sugar.level)

# Lower sugar level
body.lower_sugar_level()

# Check if the sugar level is back to normal
if body.bloodstream.sugar_level == 0:
    print("Sugar level is back to normal.")