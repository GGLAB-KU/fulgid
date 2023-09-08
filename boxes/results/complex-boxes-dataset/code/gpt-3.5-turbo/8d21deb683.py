# Initial state of boxes
boxes = {
    0: ['gloves', 'basket'],
    1: ['razor', 'usb', 'laptop', 'toothpaste'],
    2: ['wig', 'rain', 'toothbrush', 'perfume', 'paint'],
    3: ['freezer', 'toaster', 'shirt'],
    4: ['submarine', 'branch', 'jungle', 'pan', 'bear'],
    5: ['tape'],
    6: ['motorcycle'],
    7: ['controller', 'rocket'],
    8: ['harmonica', 'shelf'],
    9: ['train', 'wire'],
    10: ['grass', 'scissors', 'bowl', 'doll'],
    11: ['pot', 'mask', 'pen', 'keyboard', 'fish']
}

# Remove the tape from Box 5.
boxes[5].remove('tape')

# Replace the controller with the car in Box 7.
boxes[7].remove('controller')
boxes[7].append('car')

# Move the grass and the doll and the bowl from Box 10 to Box 4.
items_to_move = ['grass', 'doll', 'bowl']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[4].append(item)

# Put the mask and the boat into Box 9.
boxes[9].append('mask')
boxes[9].append('boat')

# Replace the perfume and the wig and the toothbrush with the lock and the piano and the doll in Box 2.
boxes[2].remove('perfume')
boxes[2].remove('wig')
boxes[2].remove('toothbrush')
boxes[2].append('lock')
boxes[2].append('piano')
boxes[2].append('doll')

# Empty Box 4.
boxes[4] = []

# Swap the usb in Box 1 with the wire in Box 9.
boxes[1].remove('usb')
boxes[9].remove('wire')
boxes[1].append('wire')
boxes[9].append('usb')

# Replace the train with the button in Box 9.
boxes[9].remove('train')
boxes[9].append('button')

# Put the snow and the tree into Box 6.
boxes[6].append('snow')
boxes[6].append('tree')

# Remove the gloves from Box 0.
boxes[0].remove('gloves')

# Move the car and the rocket from Box 7 to Box 2.
boxes[7].remove('car')
boxes[7].remove('rocket')
boxes[2].append('car')
boxes[2].append('rocket')

# Move the paint and the rain and the piano from Box 2 to Box 1.
items_to_move = ['paint', 'rain', 'piano']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Swap the basket in Box 0 with the scissors in Box 10.
boxes[0].remove('basket')
boxes[10].remove('scissors')
boxes[0].append('scissors')
boxes[10].append('basket')

# Swap the laptop in Box 1 with the scissors in Box 0.
boxes[1].remove('laptop')
boxes[0].remove('scissors')
boxes[1].append('scissors')
boxes[0].append('laptop')

# Replace the pen and the mask with the bear and the microscope in Box 11.
boxes[11].remove('pen')
boxes[11].remove('mask')
boxes[11].append('bear')
boxes[11].append('microscope')

# Put the drum into Box 9.
boxes[9].append('drum')

# Replace the car and the rocket and the doll with the branch and the forest and the charger in Box 2.
boxes[2].remove('car')
boxes[2].remove('rocket')
boxes[2].remove('doll')
boxes[2].append('branch')
boxes[2].append('forest')
boxes[2].append('charger')

# Replace the shelf and the harmonica with the branch and the book in Box 8.
boxes[8].remove('shelf')
boxes[8].remove('harmonica')
boxes[8].append('branch')
boxes[8].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")