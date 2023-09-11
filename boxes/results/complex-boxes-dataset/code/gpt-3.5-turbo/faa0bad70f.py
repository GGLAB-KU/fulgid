# Initial state of boxes
boxes = {
    0: ['river', 'meteor', 'scissors'],
    1: ['coat', 'tree', 'truck', 'magnet', 'boat'],
    2: [],
    3: ['ocean', 'toaster', 'storm'],
    4: ['rain', 'cup', 'shorts'],
    5: ['grinder', 'controller', 'snow', 'mirror'],
    6: ['towel', 'sandals'],
    7: ['coin'],
    8: [],
    9: ['ship', 'shark', 'horn', 'oven'],
    10: ['shoes', 'paint', 'shelf', 'bowl', 'motorcycle'],
    11: ['card', 'spoon', 'fork', 'telescope'],
    12: ['pot', 'plate', 'train']
}

# Remove the shelf and the motorcycle from Box 10.
boxes[10].remove('shelf')
boxes[10].remove('motorcycle')

# Put the shirt and the starfish and the jungle into Box 7.
boxes[7].append('shirt')
boxes[7].append('starfish')
boxes[7].append('jungle')

# Move the rain and the shorts and the cup from Box 4 to Box 9.
items_to_move = ['rain', 'shorts', 'cup']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Move the controller and the snow and the mirror from Box 5 to Box 7.
items_to_move = ['controller', 'snow', 'mirror']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Swap the train in Box 12 with the towel in Box 6.
boxes[12].remove('train')
boxes[6].remove('towel')
boxes[12].append('towel')
boxes[6].append('train')

# Remove the paint from Box 10.
boxes[10].remove('paint')

# Remove the grinder from Box 5.
boxes[5].remove('grinder')

# Replace the truck and the magnet with the bear and the mirror in Box 1.
boxes[1].remove('truck')
boxes[1].remove('magnet')
boxes[1].append('bear')
boxes[1].append('mirror')

# Remove the shoes from Box 10.
boxes[10].remove('shoes')

# Put the watch and the pen and the microscope into Box 5.
boxes[5].append('watch')
boxes[5].append('pen')
boxes[5].append('microscope')

# Swap the ocean in Box 3 with the coin in Box 7.
boxes[3].remove('ocean')
boxes[7].remove('coin')
boxes[3].append('coin')
boxes[7].append('ocean')

# Swap the ship in Box 9 with the train in Box 6.
boxes[9].remove('ship')
boxes[6].remove('train')
boxes[9].append('train')
boxes[6].append('ship')

# Swap the pen in Box 5 with the toaster in Box 3.
boxes[5].remove('pen')
boxes[3].remove('toaster')
boxes[5].append('toaster')
boxes[3].append('pen')

# Move the bowl from Box 10 to Box 3.
boxes[10].remove('bowl')
boxes[3].append('bowl')

# Move the boat from Box 1 to Box 2.
boxes[1].remove('boat')
boxes[2].append('boat')

# Replace the controller and the snow and the starfish with the doll and the wire and the tiger in Box 7.
boxes[7].remove('controller')
boxes[7].remove('snow')
boxes[7].remove('starfish')
boxes[7].append('doll')
boxes[7].append('wire')
boxes[7].append('tiger')

# Replace the spoon with the dress in Box 11.
boxes[11].remove('spoon')
boxes[11].append('dress')

# Remove the river and the meteor from Box 0.
boxes[0].remove('river')
boxes[0].remove('meteor')

# Put the book and the bowl into Box 0.
boxes[0].append('book')
boxes[0].append('bowl')

# Remove the towel and the plate from Box 12.
boxes[12].remove('towel')
boxes[12].remove('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")