# Initial state of boxes
boxes = {
    0: ['elephant'],
    1: ['hat'],
    2: ['controller', 'sun', 'ring', 'candle'],
    3: ['perfume', 'usb', 'freezer'],
    4: ['lipstick', 'mask', 'sandals'],
    5: [],
    6: ['seaweed', 'forest', 'plate', 'telescope']
}

# Remove the lipstick and the mask from Box 4.
boxes[4].remove('lipstick')
boxes[4].remove('mask')

# Remove the perfume and the usb from Box 3.
boxes[3].remove('perfume')
boxes[3].remove('usb')

# Swap the sandals in Box 4 with the forest in Box 6.
boxes[4].remove('sandals')
boxes[6].remove('forest')
boxes[4].append('forest')
boxes[6].append('sandals')

# Move the elephant from Box 0 to Box 2.
boxes[0].remove('elephant')
boxes[2].append('elephant')

# Remove the forest from Box 4.
boxes[4].remove('forest')

# Remove the hat from Box 1.
boxes[1].remove('hat')

# Replace the sun and the controller with the basket and the snow in Box 2.
boxes[2].remove('sun')
boxes[2].remove('controller')
boxes[2].append('basket')
boxes[2].append('snow')

# Empty Box 6.
boxes[6] = []

# Put the note into Box 2.
boxes[2].append('note')

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")