# Initial state of boxes
boxes = {
    0: ['camera'],
    1: ['sock', 'brush', 'beach', 'thunder'],
    2: ['tie', 'dice', 'fridge', 'bell'],
    3: ['microscope', 'star', 'doll', 'console', 'storm'],
    4: ['scarf', 'keyboard', 'mirror'],
    5: ['shampoo', 'bus', 'pen'],
    6: [],
    7: ['lamp', 'needle', 'zipper'],
    8: ['shoe', 'motorcycle', 'mountain'],
    9: ['cow', 'watch'],
    10: ['wig', 'scissors', 'key', 'thread', 'blender'],
    11: ['bag', 'towel'],
    12: ['lipstick', 'tree']
}

# Put the lamp and the motorcycle and the earring into Box 6.
items_to_move = ['lamp', 'motorcycle', 'earring']
for item in items_to_move:
    boxes[6].append(item)

# Remove the keyboard and the mirror and the scarf from Box 4.
items_to_remove = ['keyboard', 'mirror', 'scarf']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the wig in Box 10 with the earring in Box 6.
boxes[10].remove('wig')
boxes[6].remove('earring')
boxes[10].append('earring')
boxes[6].append('wig')

# Put the mirror and the sun into Box 5.
items_to_move = ['mirror', 'sun']
for item in items_to_move:
    boxes[5].append(item)

# Replace the shoe and the motorcycle with the toaster and the bag in Box 8.
boxes[8].remove('shoe')
boxes[8].remove('motorcycle')
boxes[8].append('toaster')
boxes[8].append('bag')

# Replace the lipstick and the tree with the bus and the horse in Box 12.
boxes[12].remove('lipstick')
boxes[12].remove('tree')
boxes[12].append('bus')
boxes[12].append('horse')

# Swap the camera in Box 0 with the blender in Box 10.
boxes[0].remove('camera')
boxes[10].remove('blender')
boxes[0].append('blender')
boxes[10].append('camera')

# Put the razor and the card into Box 4.
items_to_move = ['razor', 'card']
for item in items_to_move:
    boxes[4].append(item)

# Swap the card in Box 4 with the beach in Box 1.
boxes[4].remove('card')
boxes[1].remove('beach')
boxes[4].append('beach')
boxes[1].append('card')

# Swap the beach in Box 4 with the microscope in Box 3.
boxes[4].remove('beach')
boxes[3].remove('microscope')
boxes[4].append('microscope')
boxes[3].append('beach')

# Swap the towel in Box 11 with the camera in Box 10.
boxes[11].remove('towel')
boxes[10].remove('camera')
boxes[11].append('camera')
boxes[10].append('towel')

# Replace the bus and the horse with the whistle and the vase in Box 12.
boxes[12].remove('bus')
boxes[12].remove('horse')
boxes[12].append('whistle')
boxes[12].append('vase')

# Swap the wig in Box 6 with the microscope in Box 4.
boxes[6].remove('wig')
boxes[4].remove('microscope')
boxes[6].append('microscope')
boxes[4].append('wig')

# Put the bag into Box 12.
boxes[12].append('bag')

# Remove the lamp from Box 7.
boxes[7].remove('lamp')

# Move the bag and the camera from Box 11 to Box 3.
boxes[11].remove('bag')
boxes[11].remove('camera')
boxes[3].append('bag')
boxes[3].append('camera')

# Remove the motorcycle and the lamp from Box 6.
boxes[6].remove('motorcycle')
boxes[6].remove('lamp')

# Swap the brush in Box 1 with the bus in Box 5.
boxes[1].remove('brush')
boxes[5].remove('bus')
boxes[1].append('bus')
boxes[5].append('brush')

# Remove the bus and the sock and the card from Box 1.
items_to_remove = ['bus', 'sock', 'card']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the whistle from Box 12.
boxes[12].remove('whistle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")