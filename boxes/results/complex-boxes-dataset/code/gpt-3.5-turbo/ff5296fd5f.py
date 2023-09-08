# Initial state of boxes
boxes = {
    0: ['doll', 'dice'],
    1: ['rain', 'bowl'],
    2: ['whistle', 'comb', 'oven', 'hat'],
    3: ['headphone', 'usb', 'tree'],
    4: ['jungle'],
    5: [],
    6: ['crown'],
    7: ['towel', 'coat']
}

# Swap the comb in Box 2 with the towel in Box 7.
boxes[2].remove('comb')
boxes[7].remove('towel')
boxes[2].append('towel')
boxes[7].append('comb')

# Replace the comb with the headphone in Box 7.
boxes[7].remove('comb')
boxes[7].append('headphone')

# Put the brush and the sun and the necklace into Box 0.
items_to_put = ['brush', 'sun', 'necklace']
for item in items_to_put:
    boxes[0].append(item)

# Remove the usb from Box 3.
boxes[3].remove('usb')

# Swap the headphone in Box 3 with the hat in Box 2.
boxes[3].remove('headphone')
boxes[2].remove('hat')
boxes[3].append('hat')
boxes[2].append('headphone')

# Remove the jungle from Box 4.
boxes[4].remove('jungle')

# Replace the dice with the mirror in Box 0.
boxes[0].remove('dice')
boxes[0].append('mirror')

# Empty Box 6.
boxes[6] = []

# Swap the oven in Box 2 with the tree in Box 3.
boxes[2].remove('oven')
boxes[3].remove('tree')
boxes[2].append('tree')
boxes[3].append('oven')

# Replace the oven with the storm in Box 3.
boxes[3].remove('oven')
boxes[3].append('storm')

# Put the boot and the swimsuit and the shoes into Box 6.
items_to_put = ['boot', 'swimsuit', 'shoes']
for item in items_to_put:
    boxes[6].append(item)

# Remove the storm and the hat from Box 3.
boxes[3].remove('storm')
boxes[3].remove('hat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")