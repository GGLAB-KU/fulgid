# Initial state of boxes
boxes = {
    0: ['cup', 'train', 'shorts'],
    1: ['puzzle', 'headphone', 'bicycle', 'mirror', 'piano'],
    2: ['phone', 'rock', 'sun', 'chair'],
    3: ['plane'],
    4: [],
    5: [],
    6: ['leaf', 'toy', 'brush'],
    7: ['beach', 'storm', 'clock', 'toothbrush', 'sculpture'],
    8: ['butterfly', 'telescope', 'truck'],
    9: []
}

# Replace the telescope and the butterfly and the truck with the horn and the dolphin and the toothpaste in Box 8.
boxes[8].remove('telescope')
boxes[8].remove('butterfly')
boxes[8].remove('truck')
boxes[8].append('horn')
boxes[8].append('dolphin')
boxes[8].append('toothpaste')

# Put the cup and the sun and the tape into Box 0.
boxes[0].append('sun')
boxes[0].append('tape')

# Put the toothbrush and the belt into Box 4.
boxes[4].append('toothbrush')
boxes[4].append('belt')

# Put the apple and the battery and the ship into Box 5.
boxes[5].append('apple')
boxes[5].append('battery')
boxes[5].append('ship')

# Replace the phone and the chair with the lightning and the shoes in Box 2.
boxes[2].remove('phone')
boxes[2].remove('chair')
boxes[2].append('lightning')
boxes[2].append('shoes')

# Remove the shoes from Box 2.
boxes[2].remove('shoes')

# Replace the storm with the boot in Box 7.
boxes[7].remove('storm')
boxes[7].append('boot')

# Move the battery and the ship from Box 5 to Box 6.
items_to_move = ['battery', 'ship']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Remove the rock and the lightning and the sun from Box 2.
items_to_remove = ['rock', 'lightning', 'sun']
for item in items_to_remove:
    boxes[2].remove(item)

# Swap the sculpture in Box 7 with the toothbrush in Box 4.
boxes[7].remove('sculpture')
boxes[4].remove('toothbrush')
boxes[7].append('toothbrush')
boxes[4].append('sculpture')

# Remove the leaf and the toy and the ship from Box 6.
items_to_remove = ['leaf', 'toy', 'ship']
for item in items_to_remove:
    boxes[6].remove(item)

# Replace the apple with the cow in Box 5.
boxes[5].remove('apple')
boxes[5].append('cow')

# Remove the dolphin from Box 8.
boxes[8].remove('dolphin')

# Swap the train in Box 0 with the toothpaste in Box 8.
boxes[0].remove('train')
boxes[8].remove('toothpaste')
boxes[0].append('toothpaste')
boxes[8].append('train')

# Replace the plane with the razor in Box 3.
boxes[3].remove('plane')
boxes[3].append('razor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")