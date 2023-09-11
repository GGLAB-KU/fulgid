# Initial state of boxes
boxes = {
    0: ['car', 'plane', 'sandals', 'microscope'],
    1: [],
    2: ['whistle', 'tree', 'keyboard', 'lipstick'],
    3: ['bag', 'moon', 'razor']
}

# Move the tree and the whistle from Box 2 to Box 3.
boxes[2].remove('tree')
boxes[2].remove('whistle')
boxes[3].append('tree')
boxes[3].append('whistle')

# Move the tree and the bag and the whistle from Box 3 to Box 1.
boxes[3].remove('tree')
boxes[3].remove('bag')
boxes[3].remove('whistle')
boxes[1].append('tree')
boxes[1].append('bag')
boxes[1].append('whistle')

# Empty Box 1.
boxes[1] = []

# Empty Box 3.
boxes[3] = []

# Move the keyboard from Box 2 to Box 3.
boxes[2].remove('keyboard')
boxes[3].append('keyboard')

# Replace the keyboard with the grinder in Box 3.
boxes[3].remove('keyboard')
boxes[3].append('grinder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")