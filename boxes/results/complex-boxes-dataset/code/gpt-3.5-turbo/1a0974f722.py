# Initial state of boxes
boxes = {
    0: ['glasses', 'comet', 'vase'],
    1: ['tape', 'phone', 'gloves', 'speaker'],
    2: ['scissors', 'bag', 'button', 'blender', 'battery'],
    3: ['apple', 'rain', 'frame', 'seaweed', 'telescope'],
    4: ['wig', 'basket', 'horn', 'magnet'],
    5: ['thread', 'helmet'],
    6: [],
    7: ['whistle', 'toy', 'toaster', 'toothpaste'],
    8: ['jacket', 'shelf'],
    9: ['submarine'],
    10: ['console', 'piano', 'freezer'],
    11: ['bicycle'],
    12: []
}

# Replace the submarine with the tree in Box 9.
boxes[9].remove('submarine')
boxes[9].append('tree')

# Remove the console and the piano and the freezer from Box 10.
boxes[10].remove('console')
boxes[10].remove('piano')
boxes[10].remove('freezer')

# Put the table and the shoes and the cup into Box 0.
items_to_move = ['table', 'shoes', 'cup']
for item in items_to_move:
    boxes[0].append(item)

# Replace the thread and the helmet with the watch and the glasses in Box 5.
boxes[5].remove('thread')
boxes[5].remove('helmet')
boxes[5].append('watch')
boxes[5].append('glasses')

# Swap the speaker in Box 1 with the horn in Box 4.
boxes[1].remove('speaker')
boxes[4].remove('horn')
boxes[1].append('horn')
boxes[4].append('speaker')

# Swap the telescope in Box 3 with the horn in Box 1.
boxes[3].remove('telescope')
boxes[1].remove('horn')
boxes[3].append('horn')
boxes[1].append('telescope')

# Remove the watch and the glasses from Box 5.
boxes[5].remove('watch')
boxes[5].remove('glasses')

# Move the tree from Box 9 to Box 2.
boxes[9].remove('tree')
boxes[2].append('tree')

# Move the bicycle from Box 11 to Box 9.
boxes[11].remove('bicycle')
boxes[9].append('bicycle')

# Replace the bicycle with the tiger in Box 9.
boxes[9].remove('bicycle')
boxes[9].append('tiger')

# Swap the whistle in Box 7 with the battery in Box 2.
boxes[7].remove('whistle')
boxes[2].remove('battery')
boxes[7].append('battery')
boxes[2].append('whistle')

# Move the shelf from Box 8 to Box 1.
boxes[8].remove('shelf')
boxes[1].append('shelf')

# Swap the battery in Box 7 with the tiger in Box 9.
boxes[7].remove('battery')
boxes[9].remove('tiger')
boxes[7].append('tiger')
boxes[9].append('battery')

# Replace the battery with the fork in Box 9.
boxes[9].remove('battery')
boxes[9].append('fork')

# Replace the tiger and the toy and the toothpaste with the mixer and the plate and the sandals in Box 7.
boxes[7].remove('tiger')
boxes[7].remove('toy')
boxes[7].remove('toothpaste')
boxes[7].append('mixer')
boxes[7].append('plate')
boxes[7].append('sandals')

# Move the glasses and the table and the vase from Box 0 to Box 5.
items_to_move = ['glasses', 'table', 'vase']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Swap the magnet in Box 4 with the table in Box 5.
boxes[4].remove('magnet')
boxes[5].remove('table')
boxes[4].append('table')
boxes[5].append('magnet')

# Replace the glasses and the vase with the microscope and the chair in Box 5.
boxes[5].remove('glasses')
boxes[5].remove('vase')
boxes[5].append('microscope')
boxes[5].append('chair')

# Replace the jacket with the boat in Box 8.
boxes[8].remove('jacket')
boxes[8].append('boat')

# Replace the gloves and the tape with the shirt and the dog in Box 1.
boxes[1].remove('gloves')
boxes[1].remove('tape')
boxes[1].append('shirt')
boxes[1].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")