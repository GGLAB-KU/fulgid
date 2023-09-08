# Initial state of boxes
boxes = {
    0: ['bracelet', 'controller', 'dice', 'spoon', 'camera'],
    1: ['drum', 'tiger', 'flute'],
    2: [],
    3: ['microwave', 'shark', 'horn', 'glasses', 'thread'],
    4: ['fork', 'tie', 'desert'],
    5: ['laptop', 'mixer', 'toothbrush']
}

# Remove the fork from Box 4.
boxes[4].remove('fork')

# Move the tiger and the flute and the drum from Box 1 to Box 4.
items_to_move = ['tiger', 'flute', 'drum']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Replace the bracelet with the needle in Box 0.
boxes[0].remove('bracelet')
boxes[0].append('needle')

# Swap the drum in Box 4 with the horn in Box 3.
boxes[4].remove('drum')
boxes[3].remove('horn')
boxes[4].append('horn')
boxes[3].append('drum')

# Empty Box 5.
boxes[5] = []

# Move the tie and the tiger from Box 4 to Box 2.
items_to_move = ['tie', 'tiger']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Put the shoes and the tape into Box 2.
items_to_add = ['shoes', 'tape']
for item in items_to_add:
    boxes[2].append(item)

# Put the cow and the storm and the usb into Box 0.
items_to_add = ['cow', 'storm', 'usb']
for item in items_to_add:
    boxes[0].append(item)

# Move the usb from Box 0 to Box 1.
boxes[0].remove('usb')
boxes[1].append('usb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")