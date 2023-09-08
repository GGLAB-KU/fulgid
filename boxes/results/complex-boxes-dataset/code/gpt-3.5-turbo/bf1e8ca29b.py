# Initial state of boxes
boxes = {
    0: ['freezer'],
    1: ['butterfly', 'coin', 'mask', 'lion'],
    2: [],
    3: ['lightning'],
    4: ['bracelet', 'scarf', 'dice', 'toaster'],
    5: ['cup'],
    6: ['bicycle', 'lamp', 'harmonica'],
    7: ['sculpture', 'boat', 'submarine', 'scissors'],
    8: ['storm'],
    9: ['violin'],
    10: ['belt', 'rain', 'branch', 'helmet', 'note']
}

# Put the magnet into Box 9.
boxes[9].append('magnet')

# Replace the harmonica with the swimsuit in Box 6.
boxes[6].remove('harmonica')
boxes[6].append('swimsuit')

# Swap the helmet in Box 10 with the freezer in Box 0.
boxes[0], boxes[10] = boxes[10], boxes[0]

# Move the storm from Box 8 to Box 1.
boxes[1].append(boxes[8].pop(0))

# Put the guitar into Box 7.
boxes[7].append('guitar')

# Move the lamp and the bicycle and the swimsuit from Box 6 to Box 4.
items_to_move = ['lamp', 'bicycle', 'swimsuit']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Replace the coin and the storm with the forest and the flower in Box 1.
boxes[1].remove('coin')
boxes[1].remove('storm')
boxes[1].append('forest')
boxes[1].append('flower')

# Move the lightning from Box 3 to Box 9.
boxes[9].append(boxes[3].pop(0))

# Swap the sculpture in Box 7 with the toaster in Box 4.
boxes[7], boxes[4] = boxes[4], boxes[7]

# Replace the cup with the paint in Box 5.
boxes[5].remove('cup')
boxes[5].append('paint')

# Put the perfume and the butterfly and the tape into Box 8.
boxes[8].extend(['perfume', 'butterfly', 'tape'])

# Move the belt and the freezer from Box 10 to Box 0.
boxes[0], boxes[10] = boxes[10], boxes[0]

# Swap the note in Box 10 with the butterfly in Box 8.
boxes[10], boxes[8] = boxes[8], boxes[10]

# Replace the butterfly and the mask and the lion with the cow and the leaf and the cup in Box 1.
boxes[1].remove('butterfly')
boxes[1].remove('mask')
boxes[1].remove('lion')
boxes[1].extend(['cow', 'leaf', 'cup'])

# Move the paint from Box 5 to Box 2.
boxes[2].append(boxes[5].pop(0))

# Move the lightning from Box 9 to Box 4.
boxes[4].append(boxes[9].pop(0))

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")