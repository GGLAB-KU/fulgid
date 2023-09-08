# Initial state of boxes
boxes = {
    0: [],
    1: ['plane', 'gloves', 'laptop'],
    2: ['bus', 'oven', 'microwave'],
    3: ['mixer', 'bracelet', 'razor', 'bowl', 'sculpture'],
    4: ['telescope', 'shark', 'scissors', 'bell', 'bird'],
    5: ['flower', 'motorcycle', 'vase', 'branch', 'speaker'],
    6: [],
    7: []
}

# Swap the telescope in Box 4 with the bus in Box 2.
boxes[4].remove('telescope')
boxes[2].remove('bus')
boxes[4].append('bus')
boxes[2].append('telescope')

# Move the scissors from Box 4 to Box 3.
boxes[4].remove('scissors')
boxes[3].append('scissors')

# Replace the scissors and the bracelet and the sculpture with the mask and the toothpaste and the tape in Box 3.
boxes[3].remove('scissors')
boxes[3].remove('bracelet')
boxes[3].remove('sculpture')
boxes[3].append('mask')
boxes[3].append('toothpaste')
boxes[3].append('tape')

# Move the mask from Box 3 to Box 5.
boxes[3].remove('mask')
boxes[5].append('mask')

# Remove the shark and the bell from Box 4.
boxes[4].remove('shark')
boxes[4].remove('bell')

# Move the bird and the bus from Box 4 to Box 5.
boxes[4].remove('bird')
boxes[4].remove('bus')
boxes[5].append('bird')
boxes[5].append('bus')

# Swap the telescope in Box 2 with the bus in Box 5.
boxes[2].remove('telescope')
boxes[5].remove('bus')
boxes[2].append('bus')
boxes[5].append('telescope')

# Put the bear and the shirt into Box 4.
boxes[4].append('bear')
boxes[4].append('shirt')

# Replace the oven with the boat in Box 2.
boxes[2].remove('oven')
boxes[2].append('boat')

# Put the violin into Box 3.
boxes[3].append('violin')

# Remove the shirt and the bear from Box 4.
boxes[4].remove('shirt')
boxes[4].remove('bear')

# Swap the gloves in Box 1 with the razor in Box 3.
boxes[1].remove('gloves')
boxes[3].remove('razor')
boxes[1].append('razor')
boxes[3].append('gloves')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")