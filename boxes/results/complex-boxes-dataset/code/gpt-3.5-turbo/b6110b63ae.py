# Initial state of boxes
boxes = {
    0: ['mountain', 'battery', 'beach'],
    1: ['whistle', 'thread', 'rock'],
    2: ['wig'],
    3: ['tie', 'cup', 'plate', 'microwave'],
    4: ['butterfly'],
    5: ['pen', 'rocket', 'phone', 'dice', 'cloud'],
    6: [],
    7: ['octopus', 'boat', 'sock', 'snow', 'coat'],
    8: ['doll', 'shoe', 'mask']
}

# Swap the butterfly in Box 4 with the wig in Box 2.
boxes[4], boxes[2] = boxes[2], boxes[4]

# Replace the pen with the tree in Box 5.
boxes[5].remove('pen')
boxes[5].append('tree')

# Swap the octopus in Box 7 with the battery in Box 0.
boxes[7], boxes[0] = boxes[0], boxes[7]

# Put the rock into Box 2.
boxes[2].append('rock')

# Remove the rock from Box 2.
boxes[2].remove('rock')

# Replace the tie with the polish in Box 3.
boxes[3].remove('tie')
boxes[3].append('polish')

# Swap the boat in Box 7 with the mountain in Box 0.
boxes[7], boxes[0] = boxes[0], boxes[7]

# Move the mask and the shoe from Box 8 to Box 7.
items_to_move = ['mask', 'shoe']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Put the mirror into Box 7.
boxes[7].append('mirror')

# Put the pen into Box 8.
boxes[8].append('pen')

# Put the fridge and the river into Box 5.
items_to_add = ['fridge', 'river']
for item in items_to_add:
    boxes[5].append(item)

# Swap the doll in Box 8 with the cup in Box 3.
boxes[8], boxes[3] = boxes[3], boxes[8]

# Swap the pen in Box 8 with the boat in Box 0.
boxes[8], boxes[0] = boxes[0], boxes[8]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")