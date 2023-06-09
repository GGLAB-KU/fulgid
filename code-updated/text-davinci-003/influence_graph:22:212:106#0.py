class RockyArea:
    def __init__(self, elevation):
        self.elevation = elevation
        
class Water:
    def __init__(self, source):
        self.source = source
        
class Stream:
    def __init__(self, rocky_area, water):
        self.rocky_area = rocky_area
        self.water = water
        self.elevation = rocky_area.elevation
        
    def flow(self):
        if self.elevation > self.rocky_area.elevation:
            self.water.source = self.rocky_area
            
class River:
    def __init__(self, stream):
        self.stream = stream
        self.elevation = stream.elevation
        
    def flow(self):
        if self.elevation > self.stream.elevation:
            self.stream.water.source = self.stream
            
    def erode(self):
        self.rocky_area.elevation -= 1
        
    def cut(self):
        self.rocky_area.elevation -= 2
        
class Valley:
    def __init__(self, river):
        self.river = river
        
    def formation(self):
        if self.river.elevation > self.river.stream.elevation:
            return 'more'
        elif self.river.elevation < self.river.stream.elevation:
            return 'less'
        else:
            return 'no effect'
        
rocky_area = RockyArea(100)
water = Water(None)
stream = Stream(rocky_area, water)
river = River(stream)
smaller_river = River(stream)
valley = Valley(river)
smaller_valley = Valley(smaller_river)

smaller_river.erode()
print(smaller_valley.formation()) # less