# Initial state of boxes
boxes = {
    0: ['bear', 'fish', 'belt', 'card'],
    1: [],
    2: ['usb', 'plate', 'glasses', 'hat'],
    3: ['guitar'],
    4: [],
    5: []
}

# Replace the belt with the shoes in Box 0.
boxes[0].remove('belt')
boxes[0].append('shoes')

# Put the battery and the umbrella into Box 4.
boxes[4].append('battery')
boxes[4].append('umbrella')

# Empty Box 0.
boxes[0] = []

# Put the lion and the mirror and the planet into Box 0.
boxes[0].append('lion')
boxes[0].append('mirror')
boxes[0].append('planet')

# Swap the guitar in Box 3 with the usb in Box 2.
boxes[3].remove('guitar')
boxes[2].remove('usb')
boxes[3].append('usb')
boxes[2].append('guitar')

# Swap the usb in Box 3 with the battery in Box 4.
boxes[3].remove('usb')
boxes[4].remove('battery')
boxes[3].append('battery')
boxes[4].append('usb')

# Put the jungle into Box 2.
boxes[2].append('jungle')

# Empty Box 2.
boxes[2] = []

# Remove the lion and the mirror and the planet from Box 0.
items_to_remove = ['lion', 'mirror', 'planet']
for item in items_to_remove:
    boxes[0].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")