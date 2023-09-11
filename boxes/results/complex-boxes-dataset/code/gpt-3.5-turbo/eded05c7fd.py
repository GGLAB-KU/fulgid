# Initial state of boxes
boxes = {
    0: ['lamp', 'river', 'umbrella', 'thread'],
    1: [],
    2: ['card', 'flower'],
    3: ['game', 'coat', 'cow'],
    4: [],
    5: ['mirror', 'star', 'wire'],
    6: ['bracelet', 'mask', 'pot', 'fish'],
    7: ['pillow', 'bird', 'usb', 'bell', 'cup'],
    8: ['cat', 'bag'],
    9: ['lipstick', 'flute', 'watch'],
    10: [],
    11: ['scissors', 'ocean', 'ship'],
    12: ['toy', 'tree', 'toothpaste']
}

# Remove the bag from Box 8.
boxes[8].remove('bag')

# Remove the card from Box 2.
boxes[2].remove('card')

# Replace the watch and the flute with the basket and the keyboard in Box 9.
boxes[9].remove('watch')
boxes[9].remove('flute')
boxes[9].append('basket')
boxes[9].append('keyboard')

# Replace the usb with the tape in Box 7.
boxes[7].remove('usb')
boxes[7].append('tape')

# Replace the ocean with the boat in Box 11.
boxes[11].remove('ocean')
boxes[11].append('boat')

# Empty Box 5.
boxes[5] = []

# Replace the flower with the usb in Box 2.
boxes[2].remove('flower')
boxes[2].append('usb')

# Put the lamp and the mask into Box 1.
boxes[1].append('lamp')
boxes[1].append('mask')

# Remove the cow from Box 3.
boxes[3].remove('cow')

# Remove the mask from Box 6.
boxes[6].remove('mask')

# Move the lipstick and the keyboard and the basket from Box 9 to Box 1.
items_to_move = ['lipstick', 'keyboard', 'basket']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Put the octopus and the shoe and the horse into Box 9.
items_to_put = ['octopus', 'shoe', 'horse']
for item in items_to_put:
    boxes[9].append(item)

# Put the butterfly and the plate and the desert into Box 4.
items_to_put = ['butterfly', 'plate', 'desert']
for item in items_to_put:
    boxes[4].append(item)

# Empty Box 1.
boxes[1] = []

# Move the pot from Box 6 to Box 10.
boxes[6].remove('pot')
boxes[10].append('pot')

# Move the plate and the butterfly and the desert from Box 4 to Box 0.
items_to_move = ['plate', 'butterfly', 'desert']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Put the lightning and the comet and the submarine into Box 3.
items_to_put = ['lightning', 'comet', 'submarine']
for item in items_to_put:
    boxes[3].append(item)

# Replace the cup and the bell with the ocean and the gloves in Box 7.
boxes[7].remove('cup')
boxes[7].remove('bell')
boxes[7].append('ocean')
boxes[7].append('gloves')

# Put the hat and the candle into Box 5.
boxes[5].append('hat')
boxes[5].append('candle')

# Move the bracelet from Box 6 to Box 3.
boxes[6].remove('bracelet')
boxes[3].append('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")