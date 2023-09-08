# Initial state of boxes
boxes = {
    0: ['pan', 'shark'],
    1: [],
    2: ['lamp', 'horn', 'earring', 'necklace'],
    3: ['cup', 'sculpture'],
    4: ['button', 'ocean', 'razor'],
    5: ['microwave', 'pen', 'beach'],
    6: ['butterfly', 'mirror', 'telescope', 'pants'],
    7: [],
    8: [],
    9: ['flute', 'headphone', 'paint', 'freezer', 'toothbrush'],
    10: ['apple', 'charger', 'table', 'branch'],
    11: ['coat', 'mountain', 'rock', 'vase', 'shoe'],
    12: ['river', 'toaster', 'desert', 'umbrella', 'swimsuit']
}

# Put the microscope into Box 4.
boxes[4].append('microscope')

# Put the violin and the scissors and the paint into Box 3.
items_to_put = ['violin', 'scissors', 'paint']
for item in items_to_put:
    boxes[3].append(item)

# Swap the telescope in Box 6 with the paint in Box 9.
boxes[6].remove('telescope')
boxes[9].remove('paint')
boxes[6].append('paint')
boxes[9].append('telescope')

# Move the microwave from Box 5 to Box 12.
boxes[5].remove('microwave')
boxes[12].append('microwave')

# Move the telescope and the freezer and the flute from Box 9 to Box 5.
items_to_move = ['telescope', 'freezer', 'flute']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[5].append(item)

# Swap the paint in Box 3 with the toothbrush in Box 9.
boxes[3].remove('paint')
boxes[9].remove('toothbrush')
boxes[3].append('toothbrush')
boxes[9].append('paint')

# Swap the headphone in Box 9 with the pants in Box 6.
boxes[9].remove('headphone')
boxes[6].remove('pants')
boxes[9].append('pants')
boxes[6].append('headphone')

# Remove the shark and the pan from Box 0.
boxes[0].remove('shark')
boxes[0].remove('pan')

# Replace the pants and the paint with the shirt and the shelf in Box 9.
boxes[9].remove('pants')
boxes[9].remove('paint')
boxes[9].append('shirt')
boxes[9].append('shelf')

# Remove the butterfly and the headphone and the mirror from Box 6.
boxes[6].remove('butterfly')
boxes[6].remove('headphone')
boxes[6].remove('mirror')

# Put the scarf into Box 11.
boxes[11].append('scarf')

# Put the grinder into Box 3.
boxes[3].append('grinder')

# Put the speaker and the moon into Box 3.
boxes[3].append('speaker')
boxes[3].append('moon')

# Empty Box 6.
boxes[6] = []

# Remove the horn from Box 2.
boxes[2].remove('horn')

# Remove the button from Box 4.
boxes[4].remove('button')

# Swap the shelf in Box 9 with the earring in Box 2.
boxes[9].remove('shelf')
boxes[2].remove('earring')
boxes[9].append('earring')
boxes[2].append('shelf')

# Move the pen from Box 5 to Box 0.
boxes[5].remove('pen')
boxes[0].append('pen')

# Replace the telescope with the pan in Box 5.
boxes[5].remove('telescope')
boxes[5].append('pan')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")