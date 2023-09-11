# Initial state of boxes
boxes = {
    0: ['mixer'],
    1: ['bird', 'bear', 'dolphin', 'usb'],
    2: [],
    3: ['pen'],
    4: ['fridge', 'comb', 'toaster', 'keyboard', 'makeup'],
    5: ['leaf', 'glove'],
    6: ['swimsuit', 'lion', 'lipstick', 'ring', 'candle'],
    7: ['wallet', 'snow', 'lamp', 'earring'],
    8: []
}

# Remove the toaster from Box 4.
boxes[4].remove('toaster')

# Move the makeup from Box 4 to Box 0.
boxes[4].remove('makeup')
boxes[0].append('makeup')

# Move the leaf from Box 5 to Box 8.
boxes[5].remove('leaf')
boxes[8].append('leaf')

# Swap the leaf in Box 8 with the pen in Box 3.
boxes[8].remove('leaf')
boxes[3].remove('pen')
boxes[8].append('pen')
boxes[3].append('leaf')

# Move the fridge and the keyboard and the comb from Box 4 to Box 1.
items_to_move = ['fridge', 'keyboard', 'comb']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Swap the pen in Box 8 with the mixer in Box 0.
boxes[8].remove('pen')
boxes[0].remove('mixer')
boxes[8].append('mixer')
boxes[0].append('pen')

# Move the lamp and the snow and the wallet from Box 7 to Box 1.
items_to_move = ['lamp', 'snow', 'wallet']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Remove the makeup from Box 0.
boxes[0].remove('makeup')

# Swap the earring in Box 7 with the pen in Box 0.
boxes[7].remove('earring')
boxes[0].remove('pen')
boxes[7].append('pen')
boxes[0].append('earring')

# Move the pen from Box 7 to Box 6.
boxes[7].remove('pen')
boxes[6].append('pen')

# Replace the earring with the brush in Box 0.
boxes[0].remove('earring')
boxes[0].append('brush')

# Put the swimsuit and the vase into Box 8.
items_to_move = ['swimsuit', 'vase']
for item in items_to_move:
    boxes[8].append(item)

# Swap the usb in Box 1 with the vase in Box 8.
boxes[1].remove('usb')
boxes[8].remove('vase')
boxes[1].append('vase')
boxes[8].append('usb')

# Put the pen and the beach and the phone into Box 0.
items_to_move = ['pen', 'beach', 'phone']
for item in items_to_move:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")