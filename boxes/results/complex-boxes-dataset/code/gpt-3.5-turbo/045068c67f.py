# Initial state of boxes
boxes = {
    0: ['forest'],
    1: ['shorts'],
    2: ['microscope', 'mirror', 'earring', 'horse'],
    3: ['rain'],
    4: ['usb', 'makeup'],
    5: ['doll'],
    6: ['basket'],
    7: ['button', 'plate', 'key', 'pot', 'violin'],
    8: ['flower', 'comet'],
    9: ['puzzle', 'horn', 'beach'],
    10: ['controller', 'console', 'cow'],
    11: ['headphone'],
    12: ['mountain', 'note', 'storm'],
    13: ['planet'],
    14: ['towel', 'charger', 'table', 'coin', 'thread']
}

# Put the cow and the horn and the umbrella into Box 4.
boxes[4].append('cow')
boxes[4].append('horn')
boxes[4].append('umbrella')

# Replace the rain with the key in Box 3.
boxes[3].remove('rain')
boxes[3].append('key')

# Move the horn and the cow from Box 4 to Box 5.
boxes[4].remove('horn')
boxes[4].remove('cow')
boxes[5].append('horn')
boxes[5].append('cow')

# Swap the key in Box 3 with the basket in Box 6.
boxes[3].remove('key')
boxes[6].remove('basket')
boxes[3].append('basket')
boxes[6].append('key')

# Swap the key in Box 6 with the storm in Box 12.
boxes[6].remove('key')
boxes[12].remove('storm')
boxes[6].append('storm')
boxes[12].append('key')

# Swap the planet in Box 13 with the thread in Box 14.
boxes[13].remove('planet')
boxes[14].remove('thread')
boxes[13].append('thread')
boxes[14].append('planet')

# Put the wallet into Box 11.
boxes[11].append('wallet')

# Put the microwave into Box 10.
boxes[10].append('microwave')

# Remove the note and the key and the mountain from Box 12.
boxes[12].remove('note')
boxes[12].remove('key')
boxes[12].remove('mountain')

# Replace the doll and the cow with the shorts and the helmet in Box 5.
boxes[5].remove('doll')
boxes[5].remove('cow')
boxes[5].append('shorts')
boxes[5].append('helmet')

# Replace the storm with the wire in Box 6.
boxes[6].remove('storm')
boxes[6].append('wire')

# Remove the coin from Box 14.
boxes[14].remove('coin')

# Swap the usb in Box 4 with the basket in Box 3.
boxes[4].remove('usb')
boxes[3].remove('basket')
boxes[4].append('basket')
boxes[3].append('usb')

# Put the bear and the flute and the button into Box 7.
boxes[7].append('bear')
boxes[7].append('flute')
boxes[7].append('button')

# Put the fridge and the key and the book into Box 2.
boxes[2].append('fridge')
boxes[2].append('key')
boxes[2].append('book')

# Swap the wallet in Box 11 with the basket in Box 4.
boxes[11].remove('wallet')
boxes[4].remove('basket')
boxes[11].append('basket')
boxes[4].append('wallet')

# Move the planet from Box 14 to Box 2.
boxes[14].remove('planet')
boxes[2].append('planet')

# Move the horn and the shorts from Box 5 to Box 14.
boxes[5].remove('horn')
boxes[5].remove('shorts')
boxes[14].append('horn')
boxes[14].append('shorts')

# Remove the wire from Box 6.
boxes[6].remove('wire')

# Put the thunder and the necklace and the boat into Box 7.
boxes[7].append('thunder')
boxes[7].append('necklace')
boxes[7].append('boat')

# Swap the beach in Box 9 with the helmet in Box 5.
boxes[9].remove('beach')
boxes[5].remove('helmet')
boxes[9].append('helmet')
boxes[5].append('beach')

# Swap the horn in Box 9 with the headphone in Box 11.
boxes[9].remove('horn')
boxes[11].remove('headphone')
boxes[9].append('headphone')
boxes[11].append('horn')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")