Classes: 

Person: 
    def __init__(self):
        self.infected = False

Bacteria: 
    def __init__(self):
        self.growing = False
        self.reproducing = False
        self.producing_toxins = False

Cell: 
    def __init__(self):
        self.damaged = False

Disease: 
    def __init__(self):
        self.symptoms = []

Relationships: 
Person has_many Bacteria
Bacteria belongs_to Person
Bacteria has_many Cells
Cell belongs_to Bacteria
Person has_one Disease
Disease belongs_to Person