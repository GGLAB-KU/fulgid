# Initial state of boxes
boxes = {
    0: ['star', 'truck'],
    1: ['mask', 'beach', 'pot', 'bus'],
    2: ['blender', 'tape'],
    3: ['glove', 'planet', 'note', 'guitar', 'oven'],
    4: ['fork', 'flute', 'drum', 'scissors'],
    5: ['cow', 'vase'],
    6: ['microscope', 'perfume', 'elephant', 'earring'],
    7: ['shorts', 'storm', 'phone', 'motorcycle', 'usb'],
    8: ['soap', 'polish', 'key']
}

# Put the boot into Box 3.
boxes[3].append('boot')

# Move the storm from Box 7 to Box 4.
boxes[7].remove('storm')
boxes[4].append('storm')

# Remove the glove from Box 3.
boxes[3].remove('glove')

# Replace the pot and the beach with the book and the tree in Box 1.
boxes[1].remove('pot')
boxes[1].remove('beach')
boxes[1].append('book')
boxes[1].append('tree')

# Move the truck from Box 0 to Box 3.
boxes[0].remove('truck')
boxes[3].append('truck')

# Put the table into Box 8.
boxes[8].append('table')

# Remove the cow from Box 5.
boxes[5].remove('cow')

# Swap the tape in Box 2 with the usb in Box 7.
boxes[2].remove('tape')
boxes[7].remove('usb')
boxes[2].append('usb')
boxes[7].append('tape')

# Swap the oven in Box 3 with the flute in Box 4.
boxes[3].remove('oven')
boxes[4].remove('flute')
boxes[3].append('flute')
boxes[4].append('oven')

# Put the toothbrush and the coat and the clock into Box 3.
items_to_move = ['toothbrush', 'coat', 'clock']
for item in items_to_move:
    boxes[3].append(item)

# Move the star from Box 0 to Box 7.
boxes[0].remove('star')
boxes[7].append('star')

# Move the drum from Box 4 to Box 3.
boxes[4].remove('drum')
boxes[3].append('drum')

# Swap the book in Box 1 with the fork in Box 4.
boxes[1].remove('book')
boxes[4].remove('fork')
boxes[1].append('fork')
boxes[4].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")