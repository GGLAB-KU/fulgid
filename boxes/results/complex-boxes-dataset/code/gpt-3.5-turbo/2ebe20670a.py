# Initial state of boxes
boxes = {
    0: ['bracelet', 'dog', 'telescope', 'shampoo'],
    1: ['blender', 'necklace'],
    2: ['lipstick', 'polish', 'thread', 'swimsuit'],
    3: ['fish'],
    4: ['snow', 'bicycle'],
    5: ['bell', 'elephant']
}

# Empty Box 0
boxes[0] = []

# Move the necklace and the blender from Box 1 to Box 2.
boxes[1].remove('necklace')
boxes[1].remove('blender')
boxes[2].append('necklace')
boxes[2].append('blender')

# Replace the snow with the tree in Box 4.
boxes[4].remove('snow')
boxes[4].append('tree')

# Put the phone and the mask into Box 0.
boxes[0].append('phone')
boxes[0].append('mask')

# Swap the fish in Box 3 with the elephant in Box 5.
boxes[3].remove('fish')
boxes[5].remove('elephant')
boxes[3].append('elephant')
boxes[5].append('fish')

# Move the bell and the fish from Box 5 to Box 2.
boxes[5].remove('bell')
boxes[5].remove('fish')
boxes[2].append('bell')
boxes[2].append('fish')

# Put the rock into Box 4.
boxes[4].append('rock')

# Replace the blender and the bell and the lipstick with the sculpture and the glove and the mirror in Box 2.
boxes[2].remove('blender')
boxes[2].remove('bell')
boxes[2].remove('lipstick')
boxes[2].append('sculpture')
boxes[2].append('glove')
boxes[2].append('mirror')

# Move the mask from Box 0 to Box 5.
boxes[0].remove('mask')
boxes[5].append('mask')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")