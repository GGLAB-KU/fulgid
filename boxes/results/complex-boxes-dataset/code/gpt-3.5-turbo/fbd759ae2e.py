# Initial state of boxes
boxes = {
    0: [],
    1: ['usb', 'flute', 'pen', 'sandals', 'violin'],
    2: ['ocean', 'table'],
    3: ['polish'],
    4: ['camera', 'elephant', 'oven', 'star'],
    5: ['glasses', 'mixer', 'ring', 'bird', 'swimsuit'],
    6: ['tiger'],
    7: ['wig', 'perfume', 'car', 'horse', 'guitar'],
    8: [],
    9: ['lightning', 'crown', 'controller'],
    10: ['card', 'harmonica', 'laptop', 'toothpaste'],
    11: ['book'],
    12: ['leaf', 'belt', 'spoon'],
    13: ['blender', 'toothbrush', 'piano'],
    14: []
}

# Replace the polish with the sock in Box 3.
boxes[3].remove('polish')
boxes[3].append('sock')

# Put the book into Box 14.
boxes[11].remove('book')
boxes[14].append('book')

# Put the leaf and the toaster and the clock into Box 2.
items_to_move = ['leaf', 'toaster', 'clock']
for item in items_to_move:
    boxes[2].append(item)

# Move the flute and the pen from Box 1 to Box 3.
items_to_move = ['flute', 'pen']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Put the sock and the thread into Box 1.
items_to_put = ['sock', 'thread']
for item in items_to_put:
    boxes[1].append(item)

# Remove the horse and the wig from Box 7.
items_to_remove = ['horse', 'wig']
for item in items_to_remove:
    boxes[7].remove(item)

# Move the star and the elephant and the oven from Box 4 to Box 2.
items_to_move = ['star', 'elephant', 'oven']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Put the charger and the jacket and the doll into Box 8.
items_to_put = ['charger', 'jacket', 'doll']
for item in items_to_put:
    boxes[8].append(item)

# Put the coin into Box 14.
boxes[14].append('coin')

# Put the watch into Box 11.
boxes[11].append('watch')

# Put the sandals and the usb into Box 0.
items_to_put = ['sandals', 'usb']
for item in items_to_put:
    boxes[0].append(item)

# Remove the camera from Box 4.
boxes[4].remove('camera')

# Remove the swimsuit and the mixer and the bird from Box 5.
items_to_remove = ['swimsuit', 'mixer', 'bird']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the tiger with the meteor in Box 6.
boxes[6].remove('tiger')
boxes[6].append('meteor')

# Put the horn and the jungle and the moon into Box 6.
items_to_put = ['horn', 'jungle', 'moon']
for item in items_to_put:
    boxes[6].append(item)

# Remove the charger and the doll from Box 8.
items_to_remove = ['charger', 'doll']
for item in items_to_remove:
    boxes[8].remove(item)

# Remove the oven from Box 2.
boxes[2].remove('oven')

# Move the horn from Box 6 to Box 8.
boxes[6].remove('horn')
boxes[8].append('horn')

# Move the book and the coin from Box 14 to Box 1.
items_to_move = ['book', 'coin']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[1].append(item)

# Replace the book and the watch with the hat and the pot in Box 11.
boxes[11].remove('book')
boxes[11].remove('watch')
boxes[11].append('hat')
boxes[11].append('pot')

# Move the jungle from Box 6 to Box 1.
boxes[6].remove('jungle')
boxes[1].append('jungle')

# Remove the thread and the book and the sock from Box 1.
items_to_remove = ['thread', 'book', 'sock']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")