box = {
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

def print_boxes():
    for box_num, items in box.items():
        print(f"Box {box_num}: {items}")

# Put the lion and the fork into Box 7
box[7].extend(['lion', 'fork'])

# Swap the fridge in Box 6 with the fork in Box 7
box[6], box[7] = box[7], box[6]

# Replace the lion and the fridge with the usb and the harmonica in Box 7
box[7] = ['usb', 'harmonica']

# Remove the harmonica from Box 7
box[7].remove('harmonica')

# Put the boot and the grinder into Box 3
box[3].extend(['boot', 'grinder'])

# Empty Box 7
box[7] = []

# Move the thunder and the freezer from Box 0 to Box 1
box[1].extend(['thunder', 'freezer'])
box[0] = []

# Move the thunder from Box 1 to Box 9
box[9].append(box[1].pop(box[1].index('thunder')))

# Remove the freezer from Box 1
box[1].remove('freezer')

# Put the magnet and the ring into Box 9
box[9].extend(['magnet', 'ring'])

# Swap the lock in Box 8 with the magnet in Box 9
box[8], box[9] = box[9], box[8]

# Swap the spoon in Box 12 with the ring in Box 9
box[12], box[9] = box[9], box[12]

# Put the horn into Box 7
box[7].append('horn')

# Swap the lamp in Box 2 with the frame in Box 0
box[2], box[0] = box[0], box[2]

# Move the mask and the shoes and the magnet from Box 8 to Box 5
box[5].extend(box[8].pop(box[8].index('mask')))
box[5].extend(box[8].pop(box[8].index('shoes')))
box[5].extend(box[8].pop(box[8].index('magnet')))

# Empty Box 7
box[7] = []

# Swap the shelf in Box 0 with the lock in Box 9
box[0], box[9] = box[9], box[0]

# Swap the thunder in Box 9 with the ring in Box 12
box[9], box[12] = box[12], box[9]

# Remove the lock from Box 0
box[0].remove('lock')

# Print the final state of the boxes
print_boxes()