# Initial state of boxes
boxes = {
    0: [],
    1: ['island', 'meteor'],
    2: [],
    3: ['comb', 'piano', 'lightning', 'pants', 'fridge'],
    4: ['glasses', 'fork', 'mixer', 'rock', 'basket'],
    5: ['microscope', 'bus', 'phone', 'car', 'oven'],
    6: [],
    7: ['controller']
}

# Remove the island from Box 1.
boxes[1].remove('island')

# Swap the phone in Box 5 with the controller in Box 7.
boxes[5].remove('phone')
boxes[7].remove('controller')
boxes[5].append('controller')
boxes[7].append('phone')

# Put the magnet and the helmet and the umbrella into Box 4.
items_to_put = ['magnet', 'helmet', 'umbrella']
for item in items_to_put:
    boxes[4].append(item)

# Swap the basket in Box 4 with the phone in Box 7.
boxes[4].remove('basket')
boxes[7].remove('phone')
boxes[4].append('phone')
boxes[7].append('basket')

# Move the basket from Box 7 to Box 6.
boxes[7].remove('basket')
boxes[6].append('basket')

# Replace the meteor with the fridge in Box 1.
boxes[1].remove('meteor')
boxes[1].append('fridge')

# Replace the basket with the earring in Box 6.
boxes[6].remove('basket')
boxes[6].append('earring')

# Put the keyboard and the crown and the hat into Box 0.
items_to_put = ['keyboard', 'crown', 'hat']
for item in items_to_put:
    boxes[0].append(item)

# Replace the umbrella and the phone and the helmet with the meteor and the vase and the jacket in Box 4.
items_to_remove = ['umbrella', 'phone', 'helmet']
items_to_add = ['meteor', 'vase', 'jacket']
for item in items_to_remove:
    boxes[4].remove(item)
for item in items_to_add:
    boxes[4].append(item)

# Swap the crown in Box 0 with the piano in Box 3.
boxes[0].remove('crown')
boxes[3].remove('piano')
boxes[0].append('piano')
boxes[3].append('crown')

# Move the piano and the hat from Box 0 to Box 3.
boxes[0].remove('piano')
boxes[0].remove('hat')
boxes[3].append('piano')
boxes[3].append('hat')

# Swap the bus in Box 5 with the hat in Box 3.
boxes[5].remove('bus')
boxes[3].remove('hat')
boxes[5].append('hat')
boxes[3].append('bus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")