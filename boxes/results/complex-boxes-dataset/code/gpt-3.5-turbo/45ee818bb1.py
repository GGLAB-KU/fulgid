# Initial state of boxes
boxes = {
    0: ['console', 'belt'],
    1: ['sandals', 'comb'],
    2: [],
    3: ['tree'],
    4: ['mask', 'desert', 'tie', 'oven'],
    5: ['skirt'],
    6: ['lamp', 'speaker'],
    7: ['magnet', 'note', 'forest', 'lion'],
    8: ['doll', 'key', 'gloves', 'swimsuit'],
    9: ['microscope', 'branch', 'mixer', 'flower', 'truck'],
    10: ['soap', 'rocket']
}

# Move the lamp from Box 6 to Box 10.
boxes[6].remove('lamp')
boxes[10].append('lamp')

# Swap the lamp in Box 10 with the desert in Box 4.
boxes[10].remove('lamp')
boxes[4].remove('desert')
boxes[10].append('desert')
boxes[4].append('lamp')

# Swap the lion in Box 7 with the truck in Box 9.
boxes[7].remove('lion')
boxes[9].remove('truck')
boxes[7].append('truck')
boxes[9].append('lion')

# Move the skirt from Box 5 to Box 3.
boxes[5].remove('skirt')
boxes[3].append('skirt')

# Swap the lamp in Box 4 with the doll in Box 8.
boxes[4].remove('lamp')
boxes[8].remove('doll')
boxes[4].append('doll')
boxes[8].append('lamp')

# Put the island and the wallet and the snow into Box 9.
items_to_put = ['island', 'wallet', 'snow']
for item in items_to_put:
    boxes[9].append(item)

# Swap the mixer in Box 9 with the doll in Box 4.
boxes[9].remove('mixer')
boxes[4].remove('doll')
boxes[9].append('doll')
boxes[4].append('mixer')

# Remove the tie and the oven from Box 4.
boxes[4].remove('tie')
boxes[4].remove('oven')

# Put the pillow and the bear into Box 0.
items_to_put = ['pillow', 'bear']
for item in items_to_put:
    boxes[0].append(item)

# Replace the branch with the thunder in Box 9.
boxes[9].remove('branch')
boxes[9].append('thunder')

# Replace the mask and the mixer with the makeup and the boat in Box 4.
boxes[4].remove('mask')
boxes[4].remove('mixer')
boxes[4].append('makeup')
boxes[4].append('boat')

# Swap the comb in Box 1 with the gloves in Box 8.
boxes[1].remove('comb')
boxes[8].remove('gloves')
boxes[1].append('gloves')
boxes[8].append('comb')

# Swap the soap in Box 10 with the lion in Box 9.
boxes[10].remove('soap')
boxes[9].remove('lion')
boxes[10].append('lion')
boxes[9].append('soap')

# Remove the lion and the desert from Box 10.
boxes[10].remove('lion')
boxes[10].remove('desert')

# Move the tree and the skirt from Box 3 to Box 2.
boxes[3].remove('tree')
boxes[3].remove('skirt')
boxes[2].append('tree')
boxes[2].append('skirt')

# Swap the lamp in Box 8 with the gloves in Box 1.
boxes[8].remove('lamp')
boxes[1].remove('gloves')
boxes[8].append('gloves')
boxes[1].append('lamp')

# Remove the rocket from Box 10.
boxes[10].remove('rocket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")