# Initial state of boxes
boxes = {
    0: ['freezer', 'makeup', 'frame', 'thunder', 'shelf'],
    1: [],
    2: ['shoe', 'lamp'],
    3: ['note', 'bag'],
    4: [],
    5: ['microwave', 'swimsuit', 'oven'],
    6: ['fridge', 'sandals', 'dolphin'],
    7: ['island'],
    8: ['shoes', 'hat', 'mask', 'lock'],
    9: ['plane', 'train'],
    10: [],
    11: ['clock', 'phone', 'cloud', 'rain'],
    12: ['spoon']
}

# Put the lion and the fork into Box 7.
boxes[7].append('lion')
boxes[7].append('fork')

# Swap the fridge in Box 6 with the fork in Box 7.
boxes[6].remove('fridge')
boxes[7].remove('fork')
boxes[6].append('fork')
boxes[7].append('fridge')

# Replace the lion and the fridge with the usb and the harmonica in Box 7.
boxes[7].remove('lion')
boxes[7].remove('fridge')
boxes[7].append('usb')
boxes[7].append('harmonica')

# Remove the harmonica from Box 7.
boxes[7].remove('harmonica')

# Put the boot and the grinder into Box 3.
boxes[3].append('boot')
boxes[3].append('grinder')

# Empty Box 7.
boxes[7] = []

# Move the thunder and the freezer from Box 0 to Box 1.
boxes[1].append('thunder')
boxes[1].append('freezer')
boxes[0].remove('thunder')
boxes[0].remove('freezer')

# Move the thunder from Box 1 to Box 9.
boxes[9].append('thunder')
boxes[1].remove('thunder')

# Remove the freezer from Box 1.
boxes[1].remove('freezer')

# Put the magnet and the ring into Box 9.
boxes[9].append('magnet')
boxes[9].append('ring')

# Swap the lock in Box 8 with the magnet in Box 9.
boxes[8].remove('lock')
boxes[9].remove('magnet')
boxes[8].append('magnet')
boxes[9].append('lock')

# Swap the spoon in Box 12 with the ring in Box 9.
boxes[12].remove('spoon')
boxes[9].remove('ring')
boxes[12].append('ring')
boxes[9].append('spoon')

# Put the horn into Box 7.
boxes[7].append('horn')

# Swap the lamp in Box 2 with the frame in Box 0.
boxes[2].remove('lamp')
boxes[0].remove('frame')
boxes[2].append('frame')
boxes[0].append('lamp')

# Move the mask and the shoes and the magnet from Box 8 to Box 5.
items_to_move = ['mask', 'shoes', 'magnet']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Empty Box 7.
boxes[7] = []

# Swap the shelf in Box 0 with the lock in Box 9.
boxes[0].remove('shelf')
boxes[9].remove('lock')
boxes[0].append('lock')
boxes[9].append('shelf')

# Swap the thunder in Box 9 with the ring in Box 12.
boxes[9].remove('thunder')
boxes[12].remove('ring')
boxes[9].append('ring')
boxes[12].append('thunder')

# Remove the lock from Box 0.
boxes[0].remove('lock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")