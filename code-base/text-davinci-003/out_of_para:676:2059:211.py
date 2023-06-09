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
 
    def appear(self):
        self.appeared = True
 
 
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
    fossil.appear()
 
 
if __name__ == "__main__":
    main()