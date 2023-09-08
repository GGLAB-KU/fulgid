# Initial state of boxes
boxes = {
    0: ['headphone'],
    1: [],
    2: ['microwave', 'octopus', 'table', 'lamp', 'plate'],
    3: [],
    4: ['pants', 'train']
}

# Remove the table from Box 2.
boxes[2].remove('table')

# Swap the octopus in Box 2 with the headphone in Box 0.
boxes[0].remove('headphone')
boxes[2].remove('octopus')
boxes[0].append('octopus')
boxes[2].append('headphone')

# Put the dress into Box 0.
boxes[0].append('dress')

# Put the plate into Box 4.
boxes[2].remove('plate')
boxes[4].append('plate')

# Replace the lamp with the ring in Box 2.
boxes[2].remove('lamp')
boxes[2].append('ring')

# Put the puzzle and the jungle into Box 3.
boxes[3].append('puzzle')
boxes[3].append('jungle')

# Replace the octopus with the freezer in Box 0.
boxes[0].remove('octopus')
boxes[0].append('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")