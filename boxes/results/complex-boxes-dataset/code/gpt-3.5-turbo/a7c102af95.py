# Initial state of boxes
boxes = {
    0: ['shoe', 'oven', 'pen'],
    1: ['scissors'],
    2: ['freezer'],
    3: ['blender', 'flower', 'hat'],
    4: ['fish', 'bell', 'toothbrush', 'blanket', 'paint'],
    5: []
}

# Replace the shoe and the pen and the oven with the thread and the elephant and the plate in Box 0.
boxes[0].remove('shoe')
boxes[0].remove('oven')
boxes[0].remove('pen')
boxes[0].append('thread')
boxes[0].append('elephant')
boxes[0].append('plate')

# Move the toothbrush from Box 4 to Box 1.
boxes[4].remove('toothbrush')
boxes[1].append('toothbrush')

# Replace the plate and the elephant with the leaf and the octopus in Box 0.
boxes[0].remove('plate')
boxes[0].remove('elephant')
boxes[0].append('leaf')
boxes[0].append('octopus')

# Remove the toothbrush and the scissors from Box 1.
boxes[1].remove('toothbrush')
boxes[1].remove('scissors')

# Swap the hat in Box 3 with the octopus in Box 0.
boxes[3].remove('hat')
boxes[0].remove('octopus')
boxes[3].append('octopus')
boxes[0].append('hat')

# Swap the paint in Box 4 with the blender in Box 3.
boxes[4].remove('paint')
boxes[3].remove('blender')
boxes[4].append('blender')
boxes[3].append('paint')

# Swap the freezer in Box 2 with the octopus in Box 3.
boxes[2].remove('freezer')
boxes[3].remove('octopus')
boxes[2].append('octopus')
boxes[3].append('freezer')

# Put the glove and the key and the star into Box 2.
boxes[2].append('glove')
boxes[2].append('key')
boxes[2].append('star')

# Remove the flower and the freezer from Box 3.
boxes[3].remove('flower')
boxes[3].remove('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")