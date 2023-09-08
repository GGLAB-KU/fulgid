# Initial state of boxes
boxes = {
    0: [],
    1: ['usb', 'doll'],
    2: ['pan'],
    3: ['shark', 'toy'],
    4: ['sandals'],
    5: []
}

# Swap the pan in Box 2 with the shark in Box 3.
boxes[2].remove('pan')
boxes[3].remove('shark')
boxes[2].append('shark')
boxes[3].append('pan')

# Replace the doll with the shorts in Box 1.
boxes[1].remove('doll')
boxes[1].append('shorts')

# Remove the usb from Box 1.
boxes[1].remove('usb')

# Swap the toy in Box 3 with the sandals in Box 4.
boxes[3].remove('toy')
boxes[4].remove('sandals')
boxes[3].append('sandals')
boxes[4].append('toy')

# Remove the shorts from Box 1.
boxes[1].remove('shorts')

# Remove the toy from Box 4.
boxes[4].remove('toy')

# Remove the shark from Box 2.
boxes[2].remove('shark')

# Move the sandals from Box 3 to Box 4.
boxes[3].remove('sandals')
boxes[4].append('sandals')

# Put the sock into Box 2.
boxes[2].append('sock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")