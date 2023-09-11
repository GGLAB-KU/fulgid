# Initial state of boxes
boxes = {
    0: ['butterfly', 'scarf', 'freezer'],
    1: ['sculpture', 'boot', 'harmonica', 'pen'],
    2: ['storm', 'desert', 'wallet', 'ring'],
    3: ['oven', 'note', 'lock', 'frame', 'rocket'],
    4: ['microwave', 'grass']
}

# Swap the sculpture in Box 1 with the note in Box 3.
boxes[1].remove('sculpture')
boxes[3].remove('note')
boxes[1].append('note')
boxes[3].append('sculpture')

# Replace the microwave and the grass with the coat and the makeup in Box 4.
boxes[4].remove('microwave')
boxes[4].remove('grass')
boxes[4].append('coat')
boxes[4].append('makeup')

# Swap the pen in Box 1 with the makeup in Box 4.
boxes[1].remove('pen')
boxes[4].remove('makeup')
boxes[1].append('makeup')
boxes[4].append('pen')

# Remove the harmonica and the makeup from Box 1.
boxes[1].remove('harmonica')
boxes[1].remove('makeup')

# Put the flute and the puzzle into Box 2.
boxes[2].append('flute')
boxes[2].append('puzzle')

# Move the puzzle and the desert from Box 2 to Box 0.
boxes[2].remove('puzzle')
boxes[2].remove('desert')
boxes[0].append('puzzle')
boxes[0].append('desert')

# Remove the storm and the wallet from Box 2.
boxes[2].remove('storm')
boxes[2].remove('wallet')

# Put the shorts and the bell and the bicycle into Box 4.
boxes[4].append('shorts')
boxes[4].append('bell')
boxes[4].append('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")