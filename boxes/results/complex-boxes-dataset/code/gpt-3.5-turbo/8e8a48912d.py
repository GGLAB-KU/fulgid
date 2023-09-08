# Initial state of boxes
boxes = {
    0: [],
    1: ['button', 'console'],
    2: ['phone', 'drum', 'wallet', 'needle'],
    3: ['mask', 'soap', 'bag', 'blanket', 'snow'],
    4: [],
    5: ['butterfly', 'keyboard'],
    6: ['star'],
    7: ['spoon', 'mountain']
}

# Replace the butterfly with the magnet in Box 5.
boxes[5].remove('butterfly')
boxes[5].append('magnet')

# Put the car and the rain into Box 5.
boxes[5].append('car')
boxes[5].append('rain')

# Remove the magnet and the rain from Box 5.
boxes[5].remove('magnet')
boxes[5].remove('rain')

# Move the bag and the soap and the mask from Box 3 to Box 6.
items_to_move = ['bag', 'soap', 'mask']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[6].append(item)

# Put the whistle into Box 7.
boxes[7].append('whistle')

# Remove the spoon from Box 7.
boxes[7].remove('spoon')

# Move the keyboard and the car from Box 5 to Box 2.
items_to_move = ['keyboard', 'car']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Move the snow and the blanket from Box 3 to Box 2.
items_to_move = ['snow', 'blanket']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Replace the mask and the star with the book and the lock in Box 6.
boxes[6].remove('mask')
boxes[6].remove('star')
boxes[6].append('book')
boxes[6].append('lock')

# Replace the whistle and the mountain with the frame and the fridge in Box 7.
boxes[7].remove('whistle')
boxes[7].remove('mountain')
boxes[7].append('frame')
boxes[7].append('fridge')

# Put the zipper and the cloud and the rain into Box 6.
boxes[6].append('zipper')
boxes[6].append('cloud')
boxes[6].append('rain')

# Remove the wallet from Box 2.
boxes[2].remove('wallet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")