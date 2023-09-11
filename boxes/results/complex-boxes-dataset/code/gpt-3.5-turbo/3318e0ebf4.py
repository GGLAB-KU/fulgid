# Initial state of boxes
boxes = {
    0: [],
    1: ['usb', 'blender', 'ring'],
    2: ['coin', 'meteor', 'grinder'],
    3: ['pot', 'cup'],
    4: [],
    5: ['razor'],
    6: []
}

# Remove the ring and the usb and the blender from Box 1.
boxes[1].remove('ring')
boxes[1].remove('usb')
boxes[1].remove('blender')

# Replace the razor with the desert in Box 5.
boxes[5].remove('razor')
boxes[5].append('desert')

# Put the spoon and the butterfly into Box 0.
boxes[0].append('spoon')
boxes[0].append('butterfly')

# Swap the butterfly in Box 0 with the coin in Box 2.
boxes[0].remove('butterfly')
boxes[2].remove('coin')
boxes[0].append('coin')
boxes[2].append('butterfly')

# Move the pot and the cup from Box 3 to Box 0.
items_to_move = ['pot', 'cup']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Move the coin and the spoon from Box 0 to Box 4.
items_to_move = ['coin', 'spoon']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Put the table into Box 2.
boxes[2].append('table')

# Put the microscope and the boat into Box 2.
boxes[2].append('microscope')
boxes[2].append('boat')

# Swap the microscope in Box 2 with the pot in Box 0.
boxes[2].remove('microscope')
boxes[0].remove('pot')
boxes[2].append('pot')
boxes[0].append('microscope')

# Move the microscope and the cup from Box 0 to Box 3.
items_to_move = ['microscope', 'cup']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Put the mirror and the moon and the earring into Box 6.
boxes[6].append('mirror')
boxes[6].append('moon')
boxes[6].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")