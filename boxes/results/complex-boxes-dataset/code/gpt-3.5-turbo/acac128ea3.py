# Initial state of boxes
boxes = {
    0: ['scissors', 'sock', 'motorcycle', 'submarine', 'snow'],
    1: ['seaweed', 'wig', 'swimsuit', 'makeup', 'coat'],
    2: ['speaker', 'keyboard', 'blanket'],
    3: ['shoe', 'shelf'],
    4: ['island', 'toaster'],
    5: ['river'],
    6: ['storm', 'lightning', 'desert', 'needle', 'rocket'],
    7: ['sandals'],
    8: ['leaf', 'telescope'],
    9: ['horse', 'grinder', 'toy', 'note', 'soap'],
    10: []
}

# Put the battery and the charger and the cup into Box 9.
items_to_put = ['battery', 'charger', 'cup']
for item in items_to_put:
    boxes[9].append(item)

# Swap the shelf in Box 3 with the blanket in Box 2.
boxes[3], boxes[2] = boxes[2], boxes[3]

# Swap the river in Box 5 with the swimsuit in Box 1.
boxes[5], boxes[1] = boxes[1], boxes[5]

# Swap the cup in Box 9 with the keyboard in Box 2.
boxes[9], boxes[2] = boxes[2], boxes[9]

# Replace the speaker with the dolphin in Box 2.
boxes[2].remove('speaker')
boxes[2].append('dolphin')

# Remove the storm and the rocket and the desert from Box 6.
items_to_remove = ['storm', 'rocket', 'desert']
for item in items_to_remove:
    boxes[6].remove(item)

# Empty Box 5.
boxes[5] = []

# Remove the dolphin and the shelf from Box 2.
boxes[2].remove('dolphin')
boxes[2].remove('shelf')

# Put the microscope and the watch and the planet into Box 3.
items_to_put = ['microscope', 'watch', 'planet']
for item in items_to_put:
    boxes[3].append(item)

# Move the blanket and the watch from Box 3 to Box 0.
items_to_move = ['blanket', 'watch']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Put the ocean and the bowl into Box 8.
items_to_put = ['ocean', 'bowl']
for item in items_to_put:
    boxes[8].append(item)

# Swap the lightning in Box 6 with the island in Box 4.
boxes[6], boxes[4] = boxes[4], boxes[6]

# Put the hat and the mask and the island into Box 3.
items_to_put = ['hat', 'mask', 'island']
for item in items_to_put:
    boxes[3].append(item)

# Move the island from Box 6 to Box 7.
boxes[6].remove('island')
boxes[7].append('island')

# Replace the snow and the sock with the pants and the book in Box 0.
boxes[0].remove('snow')
boxes[0].remove('sock')
boxes[0].append('pants')
boxes[0].append('book')

# Swap the keyboard in Box 9 with the toaster in Box 4.
boxes[9], boxes[4] = boxes[4], boxes[9]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")