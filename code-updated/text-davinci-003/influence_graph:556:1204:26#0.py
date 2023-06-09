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
sugar.level = 10
body.add_sugar(sugar.level)

# Check if more regulation is needed
if body.bloodstream.sugar_level > 5:
    print("More regulation of blood sugar level is needed.")
else:
    print("No effect on the regulation of blood sugar level.")