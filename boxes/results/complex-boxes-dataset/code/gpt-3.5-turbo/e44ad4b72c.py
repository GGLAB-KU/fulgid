# Initial state of boxes
boxes = {
    0: [],
    1: ['branch', 'charger', 'magnet', 'bus'],
    2: ['moon', 'bicycle', 'glove'],
    3: ['drum'],
    4: ['pants', 'note', 'bird'],
    5: [],
    6: ['bell', 'scarf'],
    7: ['controller', 'lock', 'telescope', 'shoes', 'lipstick'],
    8: ['apple', 'belt', 'freezer'],
    9: ['octopus', 'toothpaste', 'grinder'],
    10: ['clock']
}

# Put the crown and the meteor into Box 4.
boxes[4].append('crown')
boxes[4].append('meteor')

# Put the makeup and the bag and the whistle into Box 1.
boxes[1].append('makeup')
boxes[1].append('bag')
boxes[1].append('whistle')

# Remove the branch and the charger and the bus from Box 1.
items_to_remove = ['branch', 'charger', 'bus']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the glove and the moon and the bicycle with the lightning and the controller and the pot in Box 2.
boxes[2].remove('glove')
boxes[2].remove('moon')
boxes[2].remove('bicycle')
boxes[2].append('lightning')
boxes[2].append('controller')
boxes[2].append('pot')

# Remove the controller and the pot and the lightning from Box 2.
items_to_remove = ['controller', 'pot', 'lightning']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the lock from Box 7.
boxes[7].remove('lock')

# Replace the scarf with the pan in Box 6.
boxes[6].remove('scarf')
boxes[6].append('pan')

# Move the telescope from Box 7 to Box 4.
boxes[7].remove('telescope')
boxes[4].append('telescope')

# Put the makeup and the tie into Box 2.
boxes[2].append('makeup')
boxes[2].append('tie')

# Replace the belt and the apple with the button and the sandals in Box 8.
boxes[8].remove('belt')
boxes[8].remove('apple')
boxes[8].append('button')
boxes[8].append('sandals')

# Put the horn into Box 1.
boxes[1].append('horn')

# Move the drum from Box 3 to Box 6.
boxes[3].remove('drum')
boxes[6].append('drum')

# Swap the lipstick in Box 7 with the freezer in Box 8.
boxes[7].remove('lipstick')
boxes[8].remove('freezer')
boxes[7].append('freezer')
boxes[8].append('lipstick')

# Remove the pants and the crown from Box 4.
boxes[4].remove('pants')
boxes[4].remove('crown')

# Move the button and the sandals and the lipstick from Box 8 to Box 5.
items_to_move = ['button', 'sandals', 'lipstick']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Remove the grinder and the octopus from Box 9.
items_to_remove = ['grinder', 'octopus']
for item in items_to_remove:
    boxes[9].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")