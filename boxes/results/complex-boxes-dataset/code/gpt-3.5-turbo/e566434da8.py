# Initial state of boxes
boxes = {
    0: ['flower'],
    1: ['crown', 'charger', 'cloud', 'table', 'plate'],
    2: ['car', 'button'],
    3: ['watch', 'sandals'],
    4: [],
    5: ['blender', 'comet', 'tree'],
    6: ['dolphin'],
    7: ['boot', 'perfume', 'bell', 'mirror', 'moon'],
    8: ['zipper', 'pants', 'dress', 'battery'],
    9: ['grass', 'swimsuit']
}

# Move the charger and the cloud from Box 1 to Box 5.
items_to_move = ['charger', 'cloud']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Swap the dolphin in Box 6 with the bell in Box 7.
boxes[6], boxes[7] = boxes[7], boxes[6]

# Put the charger into Box 5.
boxes[5].append('charger')

# Replace the flower with the cloud in Box 0.
boxes[0].remove('flower')
boxes[0].append('cloud')

# Move the crown and the plate and the table from Box 1 to Box 5.
items_to_move = ['crown', 'plate', 'table']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Move the dolphin and the perfume and the moon from Box 7 to Box 4.
items_to_move = ['dolphin', 'perfume', 'moon']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Put the earring into Box 8.
boxes[8].append('earring')

# Empty Box 5.
boxes[5] = []

# Put the dress and the watch and the game into Box 0.
items_to_move = ['dress', 'watch', 'game']
for item in items_to_move:
    boxes[0].append(item)

# Move the boot and the mirror from Box 7 to Box 4.
items_to_move = ['boot', 'mirror']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Move the grass from Box 9 to Box 2.
boxes[9].remove('grass')
boxes[2].append('grass')

# Swap the watch in Box 3 with the boot in Box 4.
boxes[3], boxes[4] = boxes[4], boxes[3]

# Move the bell from Box 6 to Box 7.
boxes[6].remove('bell')
boxes[7].append('bell')

# Swap the mirror in Box 4 with the earring in Box 8.
boxes[4], boxes[8] = boxes[8], boxes[4]

# Move the sandals and the boot from Box 3 to Box 5.
items_to_move = ['sandals', 'boot']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")