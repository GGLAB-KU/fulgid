# Initial state of boxes
boxes = {
    0: ['mask', 'shampoo', 'bird', 'jacket'],
    1: [],
    2: ['starfish'],
    3: [],
    4: ['river'],
    5: ['harmonica'],
    6: ['makeup', 'car'],
    7: ['island', 'dolphin', 'motorcycle'],
    8: ['butterfly', 'zipper', 'scarf'],
    9: ['hat', 'comet', 'bicycle', 'lightning'],
    10: [],
    11: ['skirt', 'vase', 'branch', 'boot'],
    12: ['spoon'],
    13: ['umbrella'],
    14: ['flower', 'comb', 'camera']
}

# Swap the starfish in Box 2 with the umbrella in Box 13.
boxes[2].remove('starfish')
boxes[13].remove('umbrella')
boxes[2].append('umbrella')
boxes[13].append('starfish')

# Move the comb and the camera and the flower from Box 14 to Box 7.
items_to_move = ['comb', 'camera', 'flower']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[7].append(item)

# Put the bus and the submarine into Box 4.
boxes[4].extend(['bus', 'submarine'])

# Move the boot and the skirt from Box 11 to Box 14.
items_to_move = ['boot', 'skirt']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[14].append(item)

# Swap the spoon in Box 12 with the scarf in Box 8.
boxes[12].remove('spoon')
boxes[8].remove('scarf')
boxes[12].append('scarf')
boxes[8].append('spoon')

# Put the crown and the starfish and the bus into Box 5.
boxes[5].extend(['crown', 'starfish', 'bus'])

# Move the zipper and the spoon and the butterfly from Box 8 to Box 6.
items_to_move = ['zipper', 'spoon', 'butterfly']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Swap the jacket in Box 0 with the skirt in Box 14.
boxes[0].remove('jacket')
boxes[14].remove('skirt')
boxes[0].append('skirt')
boxes[14].append('jacket')

# Swap the shampoo in Box 0 with the scarf in Box 12.
boxes[0].remove('shampoo')
boxes[12].remove('scarf')
boxes[0].append('scarf')
boxes[12].append('shampoo')

# Replace the makeup with the headphone in Box 6.
boxes[6].remove('makeup')
boxes[6].append('headphone')

# Replace the bus and the river and the submarine with the lamp and the shorts and the basket in Box 4.
boxes[4].remove('bus')
boxes[4].remove('river')
boxes[4].remove('submarine')
boxes[4].extend(['lamp', 'shorts', 'basket'])

# Remove the boot from Box 14.
boxes[14].remove('boot')

# Empty Box 6.
boxes[6] = []

# Replace the starfish with the ring in Box 13.
boxes[13].remove('starfish')
boxes[13].append('ring')

# Put the drum into Box 14.
boxes[14].append('drum')

# Move the vase and the branch from Box 11 to Box 14.
items_to_move = ['vase', 'branch']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[14].append(item)

# Swap the motorcycle in Box 7 with the comet in Box 9.
boxes[7].remove('motorcycle')
boxes[9].remove('comet')
boxes[7].append('comet')
boxes[9].append('motorcycle')

# Move the ring from Box 13 to Box 1.
boxes[13].remove('ring')
boxes[1].append('ring')

# Remove the umbrella from Box 2.
boxes[2].remove('umbrella')

# Swap the skirt in Box 0 with the shampoo in Box 12.
boxes[0].remove('skirt')
boxes[12].remove('shampoo')
boxes[0].append('shampoo')
boxes[12].append('skirt')

# Replace the scarf with the usb in Box 0.
boxes[0].remove('scarf')
boxes[0].append('usb')

# Move the bird and the usb and the shampoo from Box 0 to Box 5.
items_to_move = ['bird', 'usb', 'shampoo']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")