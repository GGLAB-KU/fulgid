# Initial state of boxes
boxes = {
    0: ['snow', 'lipstick', 'thread'],
    1: ['helmet', 'dog', 'pot', 'horn'],
    2: ['plate'],
    3: [],
    4: [],
    5: ['mountain', 'towel', 'fridge'],
    6: ['cat', 'rain', 'starfish', 'bus', 'jungle'],
    7: ['flute', 'vase', 'sandals', 'headphone', 'wire'],
    8: ['shelf'],
    9: ['apple']
}

# Put the keyboard and the sun and the forest into Box 9.
boxes[9].extend(['keyboard', 'sun', 'forest'])

# Put the island into Box 3.
boxes[3].append('island')

# Remove the shelf from Box 8.
boxes[8].remove('shelf')

# Remove the mountain from Box 5.
boxes[5].remove('mountain')

# Move the towel from Box 5 to Box 8.
boxes[5].remove('towel')
boxes[8].append('towel')

# Replace the towel with the violin in Box 8.
boxes[8].remove('towel')
boxes[8].append('violin')

# Move the cat and the bus from Box 6 to Box 8.
boxes[6].remove('cat')
boxes[6].remove('bus')
boxes[8].extend(['cat', 'bus'])

# Remove the fridge from Box 5.
boxes[5].remove('fridge')

# Replace the jungle and the rain with the headphone and the sock in Box 6.
boxes[6].remove('jungle')
boxes[6].remove('rain')
boxes[6].extend(['headphone', 'sock'])

# Remove the dog and the pot and the horn from Box 1.
boxes[1].remove('dog')
boxes[1].remove('pot')
boxes[1].remove('horn')

# Remove the forest from Box 9.
boxes[9].remove('forest')

# Empty Box 8.
boxes[8] = []

# Move the plate from Box 2 to Box 7.
boxes[2].remove('plate')
boxes[7].append('plate')

# Move the helmet from Box 1 to Box 4.
boxes[1].remove('helmet')
boxes[4].append('helmet')

# Replace the sandals and the plate and the wire with the usb and the dice and the blender in Box 7.
boxes[7].remove('sandals')
boxes[7].remove('plate')
boxes[7].remove('wire')
boxes[7].extend(['usb', 'dice', 'blender'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")