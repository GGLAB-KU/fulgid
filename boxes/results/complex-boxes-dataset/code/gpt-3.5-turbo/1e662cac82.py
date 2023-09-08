# Initial state of boxes
boxes = {
    0: ['mountain'],
    1: [],
    2: ['sun', 'blanket'],
    3: ['tie', 'ship', 'clock', 'tiger'],
    4: ['dolphin', 'truck'],
    5: ['plate', 'coat', 'speaker', 'wig'],
    6: ['cow', 'usb', 'swimsuit'],
    7: [],
    8: [],
    9: ['sandals'],
    10: ['violin', 'charger', 'puzzle', 'keyboard', 'storm'],
    11: [],
    12: [],
    13: ['necklace'],
    14: ['crown', 'forest', 'button']
}

# Replace the usb and the swimsuit with the ship and the harmonica in Box 6.
boxes[6].remove('usb')
boxes[6].remove('swimsuit')
boxes[6].append('ship')
boxes[6].append('harmonica')

# Swap the crown in Box 14 with the tie in Box 3.
boxes[14].remove('crown')
boxes[3].remove('tie')
boxes[14].append('tie')
boxes[3].append('crown')

# Put the cup and the makeup and the blender into Box 5.
items_to_put = ['cup', 'makeup', 'blender']
for item in items_to_put:
    boxes[5].append(item)

# Swap the necklace in Box 13 with the sandals in Box 9.
boxes[13].remove('necklace')
boxes[9].remove('sandals')
boxes[13].append('sandals')
boxes[9].append('necklace')

# Remove the mountain from Box 0.
boxes[0].remove('mountain')

# Put the rain into Box 13.
boxes[13].append('rain')

# Put the submarine into Box 14.
boxes[14].append('submarine')

# Move the sun and the blanket from Box 2 to Box 11.
items_to_move = ['sun', 'blanket']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[11].append(item)

# Move the submarine and the button from Box 14 to Box 1.
items_to_move = ['submarine', 'button']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[1].append(item)

# Move the puzzle and the violin from Box 10 to Box 14.
items_to_move = ['puzzle', 'violin']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[14].append(item)

# Swap the harmonica in Box 6 with the sun in Box 11.
boxes[6].remove('harmonica')
boxes[11].remove('sun')
boxes[6].append('sun')
boxes[11].append('harmonica')

# Move the blanket and the harmonica from Box 11 to Box 1.
items_to_move = ['blanket', 'harmonica']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[1].append(item)

# Remove the cow and the sun and the ship from Box 6.
items_to_remove = ['cow', 'sun', 'ship']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the dolphin and the truck from Box 4 to Box 13.
items_to_move = ['dolphin', 'truck']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[13].append(item)

# Put the horn and the grass and the harmonica into Box 5.
items_to_put = ['horn', 'grass', 'harmonica']
for item in items_to_put:
    boxes[5].append(item)

# Replace the charger with the hat in Box 10.
boxes[10].remove('charger')
boxes[10].append('hat')

# Put the boat and the lock into Box 9.
items_to_put = ['boat', 'lock']
for item in items_to_put:
    boxes[9].append(item)

# Remove the tie and the puzzle and the violin from Box 14.
items_to_remove = ['tie', 'puzzle', 'violin']
for item in items_to_remove:
    boxes[14].remove(item)

# Replace the ship with the grinder in Box 3.
boxes[3].remove('ship')
boxes[3].append('grinder')

# Swap the storm in Box 10 with the cup in Box 5.
boxes[10].remove('storm')
boxes[5].remove('cup')
boxes[10].append('cup')
boxes[5].append('storm')

# Put the glove and the truck into Box 3.
items_to_put = ['glove', 'truck']
for item in items_to_put:
    boxes[3].append(item)

# Swap the hat in Box 10 with the boat in Box 9.
boxes[10].remove('hat')
boxes[9].remove('boat')
boxes[10].append('boat')
boxes[9].append('hat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")