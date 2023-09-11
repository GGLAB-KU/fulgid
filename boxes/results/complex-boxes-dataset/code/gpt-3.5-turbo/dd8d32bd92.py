# Initial state of boxes
boxes = {
    0: ['usb', 'tape', 'camera', 'plane'],
    1: ['wire', 'bus'],
    2: ['charger', 'spoon', 'shampoo', 'boat', 'butterfly'],
    3: ['coral', 'scarf']
}

# Put the dolphin and the pan into Box 0.
boxes[0].append('dolphin')
boxes[0].append('pan')

# Remove the wire from Box 1.
boxes[1].remove('wire')

# Swap the butterfly in Box 2 with the bus in Box 1.
boxes[2].remove('butterfly')
boxes[1].remove('bus')
boxes[2].append('bus')
boxes[1].append('butterfly')

# Remove the butterfly from Box 1.
boxes[1].remove('butterfly')

# Replace the pan with the oven in Box 0.
boxes[0].remove('pan')
boxes[0].append('oven')

# Swap the oven in Box 0 with the scarf in Box 3.
boxes[0].remove('oven')
boxes[3].remove('scarf')
boxes[0].append('scarf')
boxes[3].append('oven')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")