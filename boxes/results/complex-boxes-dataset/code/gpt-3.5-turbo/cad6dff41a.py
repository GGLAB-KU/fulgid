# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['shirt', 'toothbrush'],
    3: ['motorcycle', 'grinder', 'leaf', 'blanket'],
    4: [],
    5: ['pan', 'microscope', 'usb'],
    6: [],
    7: []
}

# Remove the shirt from Box 2.
boxes[2].remove('shirt')

# Remove the microscope and the pan and the usb from Box 5.
items_to_remove = ['microscope', 'pan', 'usb']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the toothbrush from Box 2 to Box 6.
boxes[2].remove('toothbrush')
boxes[6].append('toothbrush')

# Put the phone and the jungle into Box 4.
boxes[4].append('phone')
boxes[4].append('jungle')

# Replace the jungle and the phone with the battery and the flute in Box 4.
boxes[4].remove('jungle')
boxes[4].remove('phone')
boxes[4].append('battery')
boxes[4].append('flute')

# Put the scissors and the freezer into Box 5.
boxes[5].append('scissors')
boxes[5].append('freezer')

# Replace the grinder and the leaf with the flower and the meteor in Box 3.
boxes[3].remove('grinder')
boxes[3].remove('leaf')
boxes[3].append('flower')
boxes[3].append('meteor')

# Remove the blanket and the flower from Box 3.
boxes[3].remove('blanket')
boxes[3].remove('flower')

# Swap the freezer in Box 5 with the meteor in Box 3.
boxes[5].remove('freezer')
boxes[3].remove('meteor')
boxes[5].append('meteor')
boxes[3].append('freezer')

# Move the motorcycle from Box 3 to Box 2.
boxes[3].remove('motorcycle')
boxes[2].append('motorcycle')

# Replace the freezer with the leaf in Box 3.
boxes[3].remove('freezer')
boxes[3].append('leaf')

# Move the battery from Box 4 to Box 3.
boxes[4].remove('battery')
boxes[3].append('battery')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")