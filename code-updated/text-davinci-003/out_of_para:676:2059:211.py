class Plant:
    def __init__(self):
        self.alive = True
 
    def die(self):
        self.alive = False
 
 
class Sediment:
    def __init__(self):
        self.buried = False
 
    def bury(self):
        self.buried = True
 
 
class Decay:
    def __init__(self):
        self.soft_parts_decayed = False
 
    def decay(self):
        self.soft_parts_decayed = True
 
 
class Mineralization:
    def __init__(self):
        self.hard_parts_mineralized = False
 
    def mineralize(self):
        self.hard_parts_mineralized = True
 
 
class Rock:
    def __init__(self):
        self.formed = False
 
    def form(self):
        self.formed = True
 
 
class Erosion:
    def __init__(self):
        self.eroded = False
 
    def erode(self):
        self.eroded = True
 
 
class Fossil:
    def __init__(self):
        self.appeared = False
 
    def appear(self, soundwaves):
        if soundwaves > 10:
            self.appeared = True
        else:
            self.appeared = False
 
 
def main():
    plant = Plant()
    sediment = Sediment()
    decay = Decay()
    mineralization = Mineralization()
    rock = Rock()
    erosion = Erosion()
    fossil = Fossil()
 
    plant.die()
    sediment.bury()
    decay.decay()
    mineralization.mineralize()
    rock.form()
    erosion.erode()
    fossil.appear(5)
 
    if fossil.appeared:
        print("The change in soundwaves has no effect on the appearance of fossils.")
    else:
        print("The decrease in soundwaves has a negative effect on the appearance of fossils.")
 
 
if __name__ == "__main__":
    main()