# Initial state of boxes
boxes = {
    0: ['forest', 'usb', 'octopus', 'towel'],
    1: ['truck', 'tree', 'toaster'],
    2: ['perfume', 'card', 'frame'],
    3: ['shoe', 'ocean', 'coat', 'watch'],
    4: ['snow', 'umbrella', 'cow', 'microscope', 'star'],
    5: ['key', 'plane', 'necklace']
}

# Move the key and the plane from Box 5 to Box 2.
items_to_move = ['key', 'plane']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Swap the usb in Box 0 with the plane in Box 2.
boxes[0].remove('usb')
boxes[2].remove('plane')
boxes[0].append('plane')
boxes[2].append('usb')

# Swap the snow in Box 4 with the plane in Box 0.
boxes[4].remove('snow')
boxes[0].remove('plane')
boxes[4].append('plane')
boxes[0].append('snow')

# Replace the toaster and the tree and the truck with the violin and the thunder and the telescope in Box 1.
boxes[1].remove('toaster')
boxes[1].remove('tree')
boxes[1].remove('truck')
boxes[1].append('violin')
boxes[1].append('thunder')
boxes[1].append('telescope')

# Swap the snow in Box 0 with the microscope in Box 4.
boxes[0].remove('snow')
boxes[4].remove('microscope')
boxes[0].append('microscope')
boxes[4].append('snow')

# Put the necklace into Box 2.
boxes[5].remove('necklace')
boxes[2].append('necklace')

# Put the jungle and the razor into Box 2.
boxes[2].append('jungle')
boxes[2].append('razor')

# Replace the umbrella and the cow and the star with the shirt and the octopus and the phone in Box 4.
boxes[4].remove('umbrella')
boxes[4].remove('cow')
boxes[4].remove('star')
boxes[4].append('shirt')
boxes[4].append('octopus')
boxes[4].append('phone')

# Replace the necklace with the jacket in Box 5.
boxes[5].remove('necklace')
boxes[5].append('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")