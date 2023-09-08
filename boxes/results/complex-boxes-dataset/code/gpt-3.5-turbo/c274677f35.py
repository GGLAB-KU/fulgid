# Initial state of boxes
boxes = {
    0: [],
    1: ['shark', 'fish'],
    2: ['coat', 'usb', 'dress'],
    3: ['basket', 'wig', 'glasses'],
    4: []
}

# Move the dress and the coat and the usb from Box 2 to Box 0.
items_to_move = ['dress', 'coat', 'usb']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Swap the shark in Box 1 with the wig in Box 3.
boxes[1].remove('shark')
boxes[3].remove('wig')
boxes[1].append('wig')
boxes[3].append('shark')

# Empty Box 1.
boxes[1] = []

# Swap the shark in Box 3 with the usb in Box 0.
boxes[3].remove('shark')
boxes[0].remove('usb')
boxes[3].append('usb')
boxes[0].append('shark')

# Move the coat and the shark and the dress from Box 0 to Box 4.
items_to_move = ['coat', 'shark', 'dress']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Put the leaf and the magnet and the lamp into Box 3.
items_to_put = ['leaf', 'magnet', 'lamp']
for item in items_to_put:
    boxes[3].append(item)

# Replace the lamp and the basket with the whistle and the comb in Box 3.
boxes[3].remove('lamp')
boxes[3].remove('basket')
boxes[3].append('whistle')
boxes[3].append('comb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")