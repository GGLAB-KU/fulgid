# Initial state of boxes
boxes = {
    0: ['razor'],
    1: ['pot', 'console', 'microscope', 'clock'],
    2: ['fish', 'fridge', 'submarine'],
    3: ['mask', 'shoe'],
    4: ['pan', 'earring', 'pen', 'book'],
    5: ['dice', 'violin', 'toothbrush', 'pants'],
    6: ['thunder', 'chair', 'ring'],
    7: []
}

# Remove the razor from Box 0.
boxes[0].remove('razor')

# Move the pen from Box 4 to Box 6.
boxes[4].remove('pen')
boxes[6].append('pen')

# Put the key and the drum into Box 4.
boxes[4].append('key')
boxes[4].append('drum')

# Move the pan and the drum and the key from Box 4 to Box 6.
items_to_move = ['pan', 'drum', 'key']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Put the wire and the horn into Box 7.
boxes[7].append('wire')
boxes[7].append('horn')

# Swap the toothbrush in Box 5 with the mask in Box 3.
boxes[5].remove('toothbrush')
boxes[3].remove('mask')
boxes[5].append('mask')
boxes[3].append('toothbrush')

# Remove the shoe from Box 3.
boxes[3].remove('shoe')

# Put the keyboard and the leaf into Box 6.
boxes[6].append('keyboard')
boxes[6].append('leaf')

# Remove the earring and the book from Box 4.
boxes[4].remove('earring')
boxes[4].remove('book')

# Move the submarine and the fish from Box 2 to Box 3.
items_to_move = ['submarine', 'fish']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Replace the mask and the dice and the violin with the lock and the coral and the thunder in Box 5.
boxes[5].remove('mask')
boxes[5].remove('dice')
boxes[5].remove('violin')
boxes[5].append('lock')
boxes[5].append('coral')
boxes[5].append('thunder')

# Swap the toothbrush in Box 3 with the leaf in Box 6.
boxes[3].remove('toothbrush')
boxes[6].remove('leaf')
boxes[3].append('leaf')
boxes[6].append('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")