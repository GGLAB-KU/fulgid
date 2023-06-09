class Participant:
    def __init__(self, name):
        self.name = name

class Collection(Participant):
    def __init__(self, name):
        super().__init__(name)

class Sorting(Participant):
    def __init__(self, name):
        super().__init__(name)

class TrashRemoval(Participant):
    def __init__(self, name):
        super().__init__(name)

class Landfill(Participant):
    def __init__(self, name):
        super().__init__(name)

class BalerMachine(Participant):
    def __init__(self, name):
        super().__init__(name)

class Bales(Participant):
    def __init__(self, name):
        super().__init__(name)

class Manufacturer(Participant):
    def __init__(self, name):
        super().__init__(name)

# Relationships
class CollectToSort(Collection, Sorting):
    def __init__(self, collection, sorting):
        super().__init__(collection.name, sorting.name)

class SortToTrashRemoval(Sorting, TrashRemoval):
    def __init__(self, sorting, trashRemoval):
        super().__init__(sorting.name, trashRemoval.name)

class TrashRemovalToLandfill(TrashRemoval, Landfill):
    def __init__(self, trashRemoval, landfill):
        super().__init__(trashRemoval.name, landfill.name)

class LandfillToBalerMachine(Landfill, BalerMachine):
    def __init__(self, landfill, balerMachine):
        super().__init__(landfill.name, balerMachine.name)

class BalerMachineToBales(BalerMachine, Bales):
    def __init__(self, balerMachine, bales):
        super().__init__(balerMachine.name, bales.name)

class BalesToManufacturer(Bales, Manufacturer):
    def __init__(self, bales, manufacturer):
        super().__init__(bales.name, manufacturer.name)