# Initial state of boxes
boxes = {
    0: ['rock', 'doll', 'boot'],
    1: [],
    2: ['toothbrush', 'pen', 'dice'],
    3: ['bus'],
    4: ['usb', 'mountain'],
    5: ['fork', 'toothpaste'],
    6: ['gloves', 'comb', 'horse'],
    7: ['glove']
}

# Put the shirt into Box 3.
boxes[3].append('shirt')

# Replace the toothpaste and the fork with the wallet and the shelf in Box 5.
boxes[5].remove('toothpaste')
boxes[5].remove('fork')
boxes[5].append('wallet')
boxes[5].append('shelf')

# Replace the shirt with the pen in Box 3.
boxes[3].remove('shirt')
boxes[3].append('pen')

# Remove the bus from Box 3.
boxes[3].remove('bus')

# Move the horse and the comb and the gloves from Box 6 to Box 5.
items_to_move = ['horse', 'comb', 'gloves']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Move the mountain from Box 4 to Box 2.
boxes[4].remove('mountain')
boxes[2].append('mountain')

# Replace the toothbrush and the pen and the dice with the usb and the drum and the rocket in Box 2.
boxes[2].remove('toothbrush')
boxes[2].remove('pen')
boxes[2].remove('dice')
boxes[2].append('usb')
boxes[2].append('drum')
boxes[2].append('rocket')

# Replace the glove with the dress in Box 7.
boxes[7].remove('glove')
boxes[7].append('dress')

# Put the whistle and the snow into Box 6.
boxes[6].append('whistle')
boxes[6].append('snow')

# Remove the snow from Box 6.
boxes[6].remove('snow')

# Remove the whistle from Box 6.
boxes[6].remove('whistle')

# Move the boot and the rock and the doll from Box 0 to Box 5.
items_to_move = ['boot', 'rock', 'doll']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")