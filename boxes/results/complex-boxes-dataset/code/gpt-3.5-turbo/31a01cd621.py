# Initial state of boxes
boxes = {
    0: ['boat'],
    1: ['brush'],
    2: ['button', 'motorcycle'],
    3: ['octopus', 'plane', 'ocean', 'pillow', 'puzzle'],
    4: ['magnet', 'spoon', 'blender', 'dress', 'leaf'],
    5: [],
    6: ['microwave'],
    7: ['charger', 'belt', 'hat', 'shelf', 'perfume']
}

# Move the ocean and the puzzle from Box 3 to Box 1.
boxes[1].extend(['ocean', 'puzzle'])
boxes[3].remove('ocean')
boxes[3].remove('puzzle')

# Swap the boat in Box 0 with the puzzle in Box 1.
boxes[0], boxes[1] = boxes[1], boxes[0]

# Replace the puzzle with the river in Box 0.
boxes[0].remove('puzzle')
boxes[0].append('river')

# Put the submarine and the mixer into Box 2.
boxes[2].extend(['submarine', 'mixer'])

# Remove the boat and the ocean and the brush from Box 1.
items_to_remove = ['boat', 'ocean', 'brush']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the blender in Box 4 with the microwave in Box 6.
boxes[4].remove('blender')
boxes[6].remove('microwave')
boxes[4].append('microwave')
boxes[6].append('blender')

# Put the ocean and the watch into Box 0.
boxes[0].extend(['ocean', 'watch'])

# Remove the river from Box 0.
boxes[0].remove('river')

# Put the guitar and the freezer and the bear into Box 2.
boxes[2].extend(['guitar', 'freezer', 'bear'])

# Replace the perfume with the keyboard in Box 7.
boxes[7].remove('perfume')
boxes[7].append('keyboard')

# Move the shelf from Box 7 to Box 5.
boxes[7].remove('shelf')
boxes[5].append('shelf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")