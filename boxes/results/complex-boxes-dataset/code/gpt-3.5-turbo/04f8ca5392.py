# Initial state of boxes
boxes = {
    0: [],
    1: ['truck', 'moon', 'sun'],
    2: ['freezer', 'shelf', 'piano', 'motorcycle', 'tie'],
    3: [],
    4: ['dog', 'sandals', 'pen', 'harmonica'],
    5: ['coin', 'oven', 'hat', 'shoes'],
    6: ['ring', 'bear', 'charger', 'dice'],
    7: ['beach', 'lightning', 'watch', 'shorts'],
    8: ['pants'],
    9: ['doll', 'vase', 'rock', 'blanket'],
    10: ['toaster'],
    11: ['flower'],
    12: ['game', 'paint'],
    13: [],
    14: ['console', 'branch', 'needle', 'key']
}

# Replace the flower with the polish in Box 11.
boxes[11].remove('flower')
boxes[11].append('polish')

# Replace the oven with the rocket in Box 5.
boxes[5].remove('oven')
boxes[5].append('rocket')

# Remove the coin from Box 5.
boxes[5].remove('coin')

# Swap the tie in Box 2 with the moon in Box 1.
boxes[1].remove('moon')
boxes[2].remove('tie')
boxes[1].append('tie')
boxes[2].append('moon')

# Replace the key and the branch and the console with the swimsuit and the telescope and the oven in Box 14.
boxes[14].remove('key')
boxes[14].remove('branch')
boxes[14].remove('console')
boxes[14].append('swimsuit')
boxes[14].append('telescope')
boxes[14].append('oven')

# Move the piano and the freezer and the motorcycle from Box 2 to Box 1.
items_to_move = ['piano', 'freezer', 'motorcycle']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Move the freezer and the truck and the tie from Box 1 to Box 8.
items_to_move = ['freezer', 'truck', 'tie']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Swap the charger in Box 6 with the polish in Box 11.
boxes[6].remove('charger')
boxes[11].remove('polish')
boxes[6].append('polish')
boxes[11].append('charger')

# Replace the vase and the rock with the bag and the piano in Box 9.
boxes[9].remove('vase')
boxes[9].remove('rock')
boxes[9].append('bag')
boxes[9].append('piano')

# Swap the truck in Box 8 with the oven in Box 14.
boxes[8].remove('truck')
boxes[14].remove('oven')
boxes[8].append('oven')
boxes[14].append('truck')

# Remove the shoes from Box 5.
boxes[5].remove('shoes')

# Swap the toaster in Box 10 with the shorts in Box 7.
boxes[10].remove('toaster')
boxes[7].remove('shorts')
boxes[10].append('shorts')
boxes[7].append('toaster')

# Move the watch and the beach from Box 7 to Box 14.
items_to_move = ['watch', 'beach']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[14].append(item)

# Put the lightning and the ring and the tiger into Box 10.
items_to_put = ['lightning', 'ring', 'tiger']
for item in items_to_put:
    boxes[10].append(item)

# Put the paint and the table into Box 0.
items_to_put = ['paint', 'table']
for item in items_to_put:
    boxes[0].append(item)

# Remove the motorcycle from Box 1.
boxes[1].remove('motorcycle')

# Remove the moon from Box 2.
boxes[2].remove('moon')

# Swap the rocket in Box 5 with the oven in Box 8.
boxes[5].remove('rocket')
boxes[8].remove('oven')
boxes[5].append('oven')
boxes[8].append('rocket')

# Swap the hat in Box 5 with the toaster in Box 7.
boxes[5].remove('hat')
boxes[7].remove('toaster')
boxes[5].append('toaster')
boxes[7].append('hat')

# Put the freezer and the comet into Box 12.
items_to_put = ['freezer', 'comet']
for item in items_to_put:
    boxes[12].append(item)

# Remove the freezer and the game and the paint from Box 12.
items_to_remove = ['freezer', 'game', 'paint']
for item in items_to_remove:
    boxes[12].remove(item)

# Swap the harmonica in Box 4 with the shelf in Box 2.
boxes[4].remove('harmonica')
boxes[2].remove('shelf')
boxes[4].append('shelf')
boxes[2].append('harmonica')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")