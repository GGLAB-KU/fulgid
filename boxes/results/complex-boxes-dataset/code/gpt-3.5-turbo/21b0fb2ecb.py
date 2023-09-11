# Initial state of boxes
boxes = {
    0: [],
    1: ['pan', 'wire', 'shoe', 'perfume'],
    2: [],
    3: ['starfish', 'microwave'],
    4: ['cloud', 'blanket'],
    5: [],
    6: []
}

# Put the pants and the swimsuit and the thunder into Box 3.
boxes[3].extend(['pants', 'swimsuit', 'thunder'])

# Replace the microwave with the rock in Box 3.
boxes[3].remove('microwave')
boxes[3].append('rock')

# Put the mountain and the octopus and the violin into Box 2.
boxes[2].extend(['mountain', 'octopus', 'violin'])

# Swap the swimsuit in Box 3 with the octopus in Box 2.
boxes[3].remove('swimsuit')
boxes[2].remove('octopus')
boxes[3].append('octopus')
boxes[2].append('swimsuit')

# Put the magnet and the toaster into Box 4.
boxes[4].extend(['magnet', 'toaster'])

# Remove the swimsuit and the mountain from Box 2.
boxes[2].remove('swimsuit')
boxes[2].remove('mountain')

# Swap the violin in Box 2 with the starfish in Box 3.
boxes[2].remove('violin')
boxes[3].remove('starfish')
boxes[2].append('starfish')
boxes[3].append('violin')

# Put the belt and the bag into Box 6.
boxes[6].extend(['belt', 'bag'])

# Move the cloud and the magnet and the blanket from Box 4 to Box 0.
items_to_move = ['cloud', 'magnet', 'blanket']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Replace the wire and the perfume with the shampoo and the cow in Box 1.
boxes[1].remove('wire')
boxes[1].remove('perfume')
boxes[1].append('shampoo')
boxes[1].append('cow')

# Remove the belt and the bag from Box 6.
boxes[6].remove('belt')
boxes[6].remove('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")