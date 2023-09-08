# Initial state of boxes
boxes = {
    0: ['motorcycle', 'dolphin', 'tree'],
    1: ['grinder', 'usb'],
    2: ['microscope', 'blender'],
    3: ['coat'],
    4: ['keyboard', 'comb', 'pen'],
    5: ['necklace', 'planet']
}

# Put the button and the motorcycle and the harmonica into Box 5.
boxes[5].append('button')
boxes[5].append('motorcycle')
boxes[5].append('harmonica')

# Replace the dolphin with the tree in Box 0.
boxes[0].remove('dolphin')
boxes[0].append('tree')

# Remove the blender from Box 2.
boxes[2].remove('blender')

# Remove the coat from Box 3.
boxes[3].remove('coat')

# Move the microscope from Box 2 to Box 5.
boxes[2].remove('microscope')
boxes[5].append('microscope')

# Swap the usb in Box 1 with the harmonica in Box 5.
boxes[1].remove('usb')
boxes[5].remove('harmonica')
boxes[1].append('harmonica')
boxes[5].append('usb')

# Move the comb and the pen and the keyboard from Box 4 to Box 2.
items_to_move = ['comb', 'pen', 'keyboard']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Move the tree and the motorcycle and the tree from Box 0 to Box 1.
items_to_move = ['tree', 'motorcycle', 'tree']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Remove the comb from Box 2.
boxes[2].remove('comb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")