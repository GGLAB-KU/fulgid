# Initial state of boxes
boxes = {
    0: ['razor', 'flower'],
    1: ['leaf', 'necklace', 'guitar'],
    2: ['glove', 'rocket', 'dice', 'charger', 'seaweed'],
    3: ['keyboard', 'brush'],
    4: ['sandals', 'mask', 'mirror', 'storm'],
    5: ['helmet', 'shoes', 'toothpaste'],
    6: ['rock', 'wig'],
    7: ['beach', 'whistle', 'freezer'],
    8: ['spoon', 'comb', 'lock', 'pillow', 'octopus'],
    9: ['grinder', 'bowl', 'boat', 'shorts'],
    10: ['toothbrush', 'umbrella', 'towel', 'bus', 'pot'],
    11: []
}

# Move the toothpaste and the helmet and the shoes from Box 5 to Box 4.
items_to_move = ['toothpaste', 'helmet', 'shoes']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Put the plate and the pot into Box 3.
items_to_move = ['plate', 'pot']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[3].append(item)

# Move the rock and the wig from Box 6 to Box 10.
items_to_move = ['rock', 'wig']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[10].append(item)

# Move the razor from Box 0 to Box 8.
boxes[0].remove('razor')
boxes[8].append('razor')

# Replace the toothpaste with the puzzle in Box 4.
boxes[4].remove('toothpaste')
boxes[4].append('puzzle')

# Move the flower from Box 0 to Box 11.
boxes[0].remove('flower')
boxes[11].append('flower')

# Move the beach and the whistle from Box 7 to Box 8.
items_to_move = ['beach', 'whistle']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[8].append(item)

# Empty Box 7.
boxes[7] = []

# Remove the flower from Box 11.
boxes[11].remove('flower')

# Replace the leaf with the toaster in Box 1.
boxes[1].remove('leaf')
boxes[1].append('toaster')

# Swap the rock in Box 10 with the lock in Box 8.
boxes[10].remove('rock')
boxes[8].remove('lock')
boxes[10].append('lock')
boxes[8].append('rock')

# Move the boat from Box 9 to Box 3.
boxes[9].remove('boat')
boxes[3].append('boat')

# Swap the sandals in Box 4 with the plate in Box 3.
boxes[4].remove('sandals')
boxes[3].remove('plate')
boxes[4].append('plate')
boxes[3].append('sandals')

# Replace the bowl and the grinder with the drum and the glasses in Box 9.
boxes[9].remove('bowl')
boxes[9].remove('grinder')
boxes[9].append('drum')
boxes[9].append('glasses')

# Swap the necklace in Box 1 with the shoes in Box 4.
boxes[1].remove('necklace')
boxes[4].remove('shoes')
boxes[1].append('shoes')
boxes[4].append('necklace')

# Move the octopus and the beach and the razor from Box 8 to Box 4.
items_to_move = ['octopus', 'beach', 'razor']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[4].append(item)

# Remove the pot from Box 10.
boxes[10].remove('pot')

# Move the octopus from Box 4 to Box 11.
boxes[4].remove('octopus')
boxes[11].append('octopus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")