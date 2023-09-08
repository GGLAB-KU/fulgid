# Initial state of boxes
boxes = {
    0: ['rock', 'flute', 'violin', 'camera'],
    1: ['game', 'earring', 'watch', 'rocket'],
    2: ['sun', 'grass', 'toy'],
    3: ['key', 'clock', 'rain', 'tree'],
    4: ['island', 'freezer', 'sculpture'],
    5: [],
    6: [],
    7: ['seaweed', 'doll', 'beach', 'jungle'],
    8: [],
    9: ['phone', 'comb', 'laptop', 'toothbrush']
}

# Put the earring and the mixer into Box 9.
boxes[9].append('earring')
boxes[9].append('mixer')

# Put the table and the glasses into Box 1.
boxes[1].append('table')
boxes[1].append('glasses')

# Put the shorts and the bell and the truck into Box 0.
boxes[0].append('shorts')
boxes[0].append('bell')
boxes[0].append('truck')

# Move the game and the watch from Box 1 to Box 6.
items_to_move = ['game', 'watch']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Swap the doll in Box 7 with the grass in Box 2.
boxes[7].remove('doll')
boxes[2].remove('grass')
boxes[7].append('grass')
boxes[2].append('doll')

# Swap the jungle in Box 7 with the tree in Box 3.
boxes[7].remove('jungle')
boxes[3].remove('tree')
boxes[7].append('tree')
boxes[3].append('jungle')

# Move the sun and the toy from Box 2 to Box 0.
items_to_move = ['sun', 'toy']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Move the rocket and the earring and the glasses from Box 1 to Box 3.
items_to_move = ['rocket', 'earring', 'glasses']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the doll from Box 2 to Box 4.
boxes[2].remove('doll')
boxes[4].append('doll')

# Replace the watch with the coat in Box 6.
boxes[6].remove('watch')
boxes[6].append('coat')

# Remove the seaweed and the grass and the beach from Box 7.
items_to_remove = ['seaweed', 'grass', 'beach']
for item in items_to_remove:
    boxes[7].remove(item)

# Replace the tree with the camera in Box 7.
boxes[7].remove('tree')
boxes[7].append('camera')

# Put the fish into Box 9.
boxes[9].append('fish')

# Remove the coat from Box 6.
boxes[6].remove('coat')

# Swap the truck in Box 0 with the fish in Box 9.
boxes[0].remove('truck')
boxes[9].remove('fish')
boxes[0].append('fish')
boxes[9].append('truck')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")