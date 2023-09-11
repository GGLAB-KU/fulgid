# Initial state of boxes
boxes = {
    0: ['guitar', 'tie', 'fridge'],
    1: ['camera', 'pan', 'table', 'mixer'],
    2: [],
    3: ['sandals'],
    4: [],
    5: ['perfume', 'book', 'hat', 'mountain', 'thunder'],
    6: ['ship'],
    7: [],
    8: ['needle', 'console', 'wig']
}

# Replace the mountain with the table in Box 5.
boxes[5].remove('mountain')
boxes[5].append('table')

# Swap the wig in Box 8 with the perfume in Box 5.
boxes[8].remove('wig')
boxes[5].remove('perfume')
boxes[8].append('perfume')
boxes[5].append('wig')

# Move the needle and the perfume and the console from Box 8 to Box 2.
items_to_move = ['needle', 'perfume', 'console']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[2].append(item)

# Remove the needle from Box 2.
boxes[2].remove('needle')

# Replace the guitar and the tie and the fridge with the flute and the makeup and the shelf in Box 0.
boxes[0].remove('guitar')
boxes[0].remove('tie')
boxes[0].remove('fridge')
boxes[0].append('flute')
boxes[0].append('makeup')
boxes[0].append('shelf')

# Put the gloves into Box 2.
boxes[2].append('gloves')

# Move the mixer and the camera from Box 1 to Box 8.
items_to_move = ['mixer', 'camera']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Put the perfume into Box 8.
boxes[5].remove('perfume')
boxes[8].append('perfume')

# Swap the ship in Box 6 with the pan in Box 1.
boxes[6], boxes[1] = boxes[1], boxes[6]

# Swap the ship in Box 1 with the sandals in Box 3.
boxes[1], boxes[3] = boxes[3], boxes[1]

# Move the table and the sandals from Box 1 to Box 3.
items_to_move = ['table', 'sandals']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Swap the console in Box 2 with the wig in Box 5.
boxes[2], boxes[5] = boxes[5], boxes[2]

# Move the sandals from Box 3 to Box 0.
boxes[3].remove('sandals')
boxes[0].append('sandals')

# Swap the wig in Box 2 with the makeup in Box 0.
boxes[2], boxes[0] = boxes[0], boxes[2]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")