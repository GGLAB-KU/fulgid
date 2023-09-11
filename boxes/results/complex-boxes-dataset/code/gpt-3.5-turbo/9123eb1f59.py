# Initial state of boxes
boxes = {
    0: ['river', 'mask'],
    1: ['necklace', 'drum', 'hat'],
    2: [],
    3: ['crown', 'needle'],
    4: ['boat', 'toaster', 'lamp', 'speaker'],
    5: ['oven', 'plane', 'car'],
    6: ['coat', 'camera', 'seaweed', 'leaf'],
    7: ['shelf', 'sculpture', 'makeup', 'earring', 'spoon'],
    8: [],
    9: [],
    10: [],
    11: ['guitar', 'jacket'],
    12: ['pants', 'snow']
}

# Remove the necklace and the drum and the hat from Box 1.
items_to_remove = ['necklace', 'drum', 'hat']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the crown and the needle with the lightning and the basket in Box 3.
boxes[3].remove('crown')
boxes[3].remove('needle')
boxes[3].append('lightning')
boxes[3].append('basket')

# Swap the sculpture in Box 7 with the pants in Box 12.
boxes[7].remove('sculpture')
boxes[12].remove('pants')
boxes[7].append('pants')
boxes[12].append('sculpture')

# Swap the earring in Box 7 with the mask in Box 0.
boxes[7].remove('earring')
boxes[0].remove('mask')
boxes[7].append('mask')
boxes[0].append('earring')

# Remove the jacket and the guitar from Box 11.
boxes[11].remove('jacket')
boxes[11].remove('guitar')

# Swap the speaker in Box 4 with the lightning in Box 3.
boxes[4].remove('speaker')
boxes[3].remove('lightning')
boxes[4].append('lightning')
boxes[3].append('speaker')

# Remove the sculpture and the snow from Box 12.
boxes[12].remove('sculpture')
boxes[12].remove('snow')

# Remove the seaweed from Box 6.
boxes[6].remove('seaweed')

# Move the pants and the spoon and the makeup from Box 7 to Box 2.
items_to_move = ['pants', 'spoon', 'makeup']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[2].append(item)

# Move the pants and the spoon from Box 2 to Box 7.
items_to_move = ['pants', 'spoon']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Swap the earring in Box 0 with the mask in Box 7.
boxes[0].remove('earring')
boxes[7].remove('mask')
boxes[0].append('mask')
boxes[7].append('earring')

# Move the plane and the oven from Box 5 to Box 8.
items_to_move = ['plane', 'oven']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Put the book into Box 6.
boxes[6].append('book')

# Swap the car in Box 5 with the plane in Box 8.
boxes[5].remove('car')
boxes[8].remove('plane')
boxes[5].append('plane')
boxes[8].append('car')

# Move the boat and the toaster from Box 4 to Box 3.
items_to_move = ['boat', 'toaster']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Move the leaf from Box 6 to Box 7.
boxes[6].remove('leaf')
boxes[7].append('leaf')

# Remove the earring and the spoon from Box 7.
items_to_remove = ['earring', 'spoon']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the violin and the gloves and the fork into Box 9.
items_to_put = ['violin', 'gloves', 'fork']
for item in items_to_put:
    boxes[9].append(item)

# Replace the book with the shirt in Box 6.
boxes[6].remove('book')
boxes[6].append('shirt')

# Replace the coat and the camera with the swimsuit and the pillow in Box 6.
boxes[6].remove('coat')
boxes[6].remove('camera')
boxes[6].append('swimsuit')
boxes[6].append('pillow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")