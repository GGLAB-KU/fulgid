# Initial state of boxes
boxes = {
    0: ['lion', 'snow', 'paint', 'wig', 'hat'],
    1: ['telescope', 'vase', 'belt', 'speaker'],
    2: ['beach', 'plate', 'desert', 'glasses'],
    3: ['cow', 'cat', 'mirror', 'spoon'],
    4: [],
    5: ['river', 'phone', 'candle', 'book', 'sun']
}

# Swap the beach in Box 2 with the snow in Box 0.
boxes[0].remove('snow')
boxes[2].remove('beach')
boxes[0].append('beach')
boxes[2].append('snow')

# Replace the candle and the river and the sun with the usb and the razor and the lamp in Box 5.
boxes[5].remove('candle')
boxes[5].remove('river')
boxes[5].remove('sun')
boxes[5].append('usb')
boxes[5].append('razor')
boxes[5].append('lamp')

# Put the rocket into Box 2.
boxes[2].append('rocket')

# Put the watch and the wig into Box 0.
boxes[0].append('watch')
boxes[0].append('wig')

# Remove the phone from Box 5.
boxes[5].remove('phone')

# Move the watch and the hat and the paint from Box 0 to Box 1.
items_to_move = ['watch', 'hat', 'paint']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Replace the mirror with the tie in Box 3.
boxes[3].remove('mirror')
boxes[3].append('tie')

# Replace the razor and the usb and the book with the shelf and the mask and the skirt in Box 5.
boxes[5].remove('razor')
boxes[5].remove('usb')
boxes[5].remove('book')
boxes[5].append('shelf')
boxes[5].append('mask')
boxes[5].append('skirt')

# Remove the cat from Box 3.
boxes[3].remove('cat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")