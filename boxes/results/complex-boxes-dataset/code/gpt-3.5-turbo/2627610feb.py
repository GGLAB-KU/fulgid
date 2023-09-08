# Initial state of boxes
boxes = {
    0: ['freezer'],
    1: ['shark', 'table', 'dice'],
    2: ['lamp', 'tree', 'crown', 'blanket', 'soap'],
    3: ['rain'],
    4: ['storm'],
    5: ['whistle', 'blender', 'tie', 'horn'],
    6: ['headphone', 'mountain', 'truck', 'butterfly'],
    7: ['toy'],
    8: []
}

# Swap the table in Box 1 with the freezer in Box 0.
boxes[0], boxes[1] = boxes[1], boxes[0]

# Put the scarf into Box 1.
boxes[1].append('scarf')

# Swap the mountain in Box 6 with the rain in Box 3.
boxes[3], boxes[6] = boxes[6], boxes[3]

# Remove the toy from Box 7.
boxes[7].remove('toy')

# Remove the storm from Box 4.
boxes[4].remove('storm')

# Empty Box 0.
boxes[0] = []

# Move the mountain from Box 3 to Box 5.
boxes[3].remove('mountain')
boxes[5].append('mountain')

# Remove the crown from Box 2.
boxes[2].remove('crown')

# Replace the horn and the tie and the blender with the toy and the key and the shampoo in Box 5.
boxes[5].remove('horn')
boxes[5].remove('tie')
boxes[5].remove('blender')
boxes[5].append('toy')
boxes[5].append('key')
boxes[5].append('shampoo')

# Swap the truck in Box 6 with the key in Box 5.
boxes[5].remove('key')
boxes[6].remove('truck')
boxes[5].append('truck')
boxes[6].append('key')

# Remove the soap from Box 2.
boxes[2].remove('soap')

# Remove the key and the rain from Box 6.
boxes[6].remove('key')
boxes[6].remove('rain')

# Replace the lamp with the chair in Box 2.
boxes[2].remove('lamp')
boxes[2].append('chair')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")