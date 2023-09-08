# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['key', 'jungle', 'battery', 'frame', 'drum'],
    3: [],
    4: ['pan', 'lipstick'],
    5: ['crown', 'umbrella', 'leaf'],
    6: [],
    7: [],
    8: ['beach', 'whistle'],
    9: ['flower', 'pants', 'bowl', 'microwave']
}

# Swap the beach in Box 8 with the microwave in Box 9.
boxes[8], boxes[9] = boxes[9], boxes[8]

# Remove the flower from Box 9.
boxes[9].remove('flower')

# Move the crown from Box 5 to Box 3.
boxes[5].remove('crown')
boxes[3].append('crown')

# Empty Box 4.
boxes[4] = []

# Empty Box 9.
boxes[9] = []

# Move the crown from Box 3 to Box 9.
boxes[3].remove('crown')
boxes[9].append('crown')

# Move the microwave and the whistle from Box 8 to Box 4.
boxes[8].remove('microwave')
boxes[8].remove('whistle')
boxes[4].append('microwave')
boxes[4].append('whistle')

# Move the crown from Box 9 to Box 7.
boxes[9].remove('crown')
boxes[7].append('crown')

# Move the crown from Box 7 to Box 1.
boxes[7].remove('crown')
boxes[1].append('crown')

# Remove the leaf and the umbrella from Box 5.
boxes[5].remove('leaf')
boxes[5].remove('umbrella')

# Empty Box 2.
boxes[2] = []

# Swap the crown in Box 1 with the whistle in Box 4.
boxes[1].remove('crown')
boxes[4].remove('whistle')
boxes[1].append('whistle')
boxes[4].append('crown')

# Replace the whistle with the vase in Box 1.
boxes[1].remove('whistle')
boxes[1].append('vase')

# Remove the vase from Box 1.
boxes[1].remove('vase')

# Put the hat and the jacket and the towel into Box 7.
items_to_move = ['hat', 'jacket', 'towel']
for item in items_to_move:
    boxes[7].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")