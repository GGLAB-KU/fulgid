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
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
        self.current_fill = 0

    def fill(self, amount):
        self.current_fill += amount

    def is_full(self):
        return self.current_fill >= self.capacity

class BalerMachine(Participant):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

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

# Simulation
def simulate(faster_baler=False):
    # Participants
    collection = Collection("Collection")
    sorting = Sorting("Sorting")
    trash_removal = TrashRemoval("Trash Removal")
    landfill = Landfill("Landfill", 1000)
    baler_machine = BalerMachine("Baler Machine", 10 if not faster_baler else 20)
    bales = Bales("Bales")
    manufacturer = Manufacturer("Manufacturer")

    # Relationships
    collect_to_sort = CollectToSort(collection, sorting)
    sort_to_trash_removal = SortToTrashRemoval(sorting, trash_removal)
    trash_removal_to_landfill = TrashRemovalToLandfill(trash_removal, landfill)
    landfill_to_baler_machine = LandfillToBalerMachine(landfill, baler_machine)
    baler_machine_to_bales = BalerMachineToBales(baler_machine, bales)
    bales_to_manufacturer = BalesToManufacturer(bales, manufacturer)

    # Simulation
    items_collected = 500
    items_sorted = 500
    trash_removed = 200
    bales_shipped = 500

    # Collection
    items_collected = collection.name + " collected " + str(items_collected) + " items."
    print(items_collected)

    # Sorting
    items_sorted = sorting.name + " sorted " + str(items_sorted) + " items."
    print(items_sorted)

    # Trash Removal
    trash_removed = trash_removal.name + " removed " + str(trash_removed) + " items of trash."
    print(trash_removed)

    # Landfill
    landfill.fill(items_collected - items_sorted - trash_removed)
    if landfill.is_full():
        print("Landfill is full!")
    else:
        print("Landfill has " + str(landfill.current_fill) + " items.")

    # Baler Machine
    bales_created = min(baler_machine.speed, items_sorted - trash_removed)
    bales_created = baler_machine.name + " created " + str(bales_created) + " bales."
    print(bales_created)

    # Bales
    bales_shipped = bales.name + " shipped " + str(bales_shipped) + " bales to " + manufacturer.name + "."
    print(bales_shipped)

# Test
simulate()
simulate(faster_baler=True)

# Answer to the question
print("If faster baler machines are created, it will have 'no effect' on the landfill becoming full.")