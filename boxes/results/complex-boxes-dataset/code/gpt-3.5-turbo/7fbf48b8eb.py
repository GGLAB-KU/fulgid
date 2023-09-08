# Initial state of boxes
boxes = {
    0: ['dolphin', 'brush', 'pillow', 'desert'],
    1: [],
    2: ['starfish', 'lion', 'table'],
    3: [],
    4: ['soap', 'thunder', 'storm', 'rain', 'lamp'],
    5: ['shoes', 'cup', 'usb', 'planet', 'laptop']
}

# Move the thunder and the storm and the soap from Box 4 to Box 1.
items_to_move = ['thunder', 'storm', 'soap']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Move the soap and the storm from Box 1 to Box 2.
items_to_move = ['soap', 'storm']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Remove the lamp from Box 4.
boxes[4].remove('lamp')

# Put the microscope into Box 1.
boxes[1].append('microscope')

# Put the earring into Box 5.
boxes[5].append('earring')

# Put the bracelet into Box 0.
boxes[0].append('bracelet')

# Swap the lion in Box 2 with the bracelet in Box 0.
boxes[2].remove('lion')
boxes[0].remove('bracelet')
boxes[2].append('bracelet')
boxes[0].append('lion')

# Remove the rain from Box 4.
boxes[4].remove('rain')

# Remove the microscope and the thunder from Box 1.
items_to_remove = ['microscope', 'thunder']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")