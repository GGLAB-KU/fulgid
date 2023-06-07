class Participant:
    def __init__(self, name):
        self.name = name

class RecycleBin(Participant):
    def put_can(self, can):
        self.can = can

class Facility(Participant):
    def transport_can(self, can):
        self.can = can

class Machine(Participant):
    def shred_can(self, can):
        self.can = can

class Heater(Participant):
    def heat_can(self, can):
        self.can = can

class Mold(Participant):
    def pour_metal(self, metal):
        self.metal = metal

class Roller(Participant):
    def flatten_mold(self, mold):
        self.mold = mold

# Create participants
recycle_bin = RecycleBin('Recycle Bin')
facility = Facility('Facility')
machine = Machine('Machine')
heater = Heater('Heater')
mold = Mold('Mold')
roller = Roller('Roller')

# Put the aluminum can into a recycle bin
recycle_bin.put_can('Aluminum Can')

# The cans are transported to a facility
facility.transport_can(recycle_bin.can)

# The cans are shredded by a machine
machine.shred_can(facility.can)

# The cans are heated to 1400 degrees to melt them
heater.heat_can(machine.can)

# The molten metal is poured into molds
mold.pour_metal(heater.can)

# The molds are flattened and rolled into sheets to reuse.
roller.flatten_mold(mold.metal)