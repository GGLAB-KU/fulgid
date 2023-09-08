# Initial state of boxes
boxes = {
    0: ['puzzle', 'magnet'],
    1: ['butterfly', 'helmet', 'violin'],
    2: [],
    3: ['headphone', 'motorcycle'],
    4: ['ocean'],
    5: ['river', 'vase', 'storm', 'controller', 'horse'],
    6: ['toy', 'glasses', 'moon', 'lightning'],
    7: [],
    8: ['book', 'tree'],
    9: ['flute', 'paint', 'dice', 'polish'],
    10: ['toothbrush', 'glove', 'rock'],
    11: [],
    12: ['freezer', 'pants', 'basket'],
    13: ['frame', 'towel', 'shorts', 'key', 'skirt'],
    14: ['bear']
}

# Put the needle and the telescope into Box 1.
boxes[1].append('needle')
boxes[1].append('telescope')

# Move the polish and the flute and the dice from Box 9 to Box 10.
items_to_move = ['polish', 'flute', 'dice']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[10].append(item)

# Put the boot and the telescope into Box 3.
boxes[3].append('boot')
boxes[3].append('telescope')

# Replace the controller and the horse with the shirt and the makeup in Box 5.
boxes[5].remove('controller')
boxes[5].remove('horse')
boxes[5].append('shirt')
boxes[5].append('makeup')

# Replace the bear with the tape in Box 14.
boxes[14].remove('bear')
boxes[14].append('tape')

# Swap the ocean in Box 4 with the puzzle in Box 0.
boxes[4].remove('ocean')
boxes[0].remove('puzzle')
boxes[4].append('puzzle')
boxes[0].append('ocean')

# Swap the magnet in Box 0 with the freezer in Box 12.
boxes[0].remove('magnet')
boxes[12].remove('freezer')
boxes[0].append('freezer')
boxes[12].append('magnet')

# Replace the freezer with the usb in Box 0.
boxes[0].remove('freezer')
boxes[0].append('usb')

# Remove the river from Box 5.
boxes[5].remove('river')

# Remove the polish and the toothbrush and the dice from Box 10.
items_to_remove = ['polish', 'toothbrush', 'dice']
for item in items_to_remove:
    boxes[10].remove(item)

# Empty Box 9.
boxes[9] = []

# Swap the tape in Box 14 with the tree in Box 8.
boxes[14].remove('tape')
boxes[8].remove('tree')
boxes[14].append('tree')
boxes[8].append('tape')

# Swap the book in Box 8 with the storm in Box 10.
boxes[8].remove('book')
boxes[10].remove('storm')
boxes[8].append('storm')
boxes[10].append('book')

# Put the mask and the desert and the horse into Box 5.
boxes[5].append('mask')
boxes[5].append('desert')
boxes[5].append('horse')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")