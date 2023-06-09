class Earth:
    def __init__(self):
        self.cracks = []
        self.pressure = 0
        self.movement = 0
        self.energy = 0
    
    def develop_cracks(self):
        self.cracks.append(Crack())
    
    def increase_pressure(self):
        self.pressure += 1
    
    def increase_movement(self):
        self.movement += 1
    
    def release_energy(self):
        self.energy += 1
    
    def cause_seismic_waves(self):
        self.seismic_waves = SeismicWaves()
    
    def cause_earthquake(self):
        self.earthquake = Earthquake()

class Crack:
    def __init__(self):
        self.length = 0
        self.width = 0
    
    def increase_length(self):
        self.length += 1
    
    def increase_width(self):
        self.width += 1

class Rocks:
    def __init__(self):
        self.pressure = 0
        self.movement = 0
    
    def increase_pressure(self):
        self.pressure += 1
    
    def increase_movement(self):
        self.movement += 1
    
    def crumble(self):
        self.crumble = True

class SeismicWaves:
    def __init__(self):
        self.magnitude = 0
    
    def increase_magnitude(self):
        self.magnitude += 1

class Earthquake:
    def __init__(self):
        self.intensity = 0
    
    def increase_intensity(self):
        self.intensity += 1