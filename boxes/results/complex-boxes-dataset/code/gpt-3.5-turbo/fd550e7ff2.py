# Initial state of boxes
boxes = {
    0: ['brush', 'ocean', 'grass', 'razor'],
    1: ['spoon', 'glasses'],
    2: ['guitar'],
    3: ['bus', 'doll']
}

# Put the wallet and the wire into Box 1.
boxes[1].append('wallet')
boxes[1].append('wire')

# Swap the guitar in Box 2 with the brush in Box 0.
boxes[0].remove('brush')
boxes[2].remove('guitar')
boxes[0].append('guitar')
boxes[2].append('brush')

# Move the grass and the razor and the guitar from Box 0 to Box 2.
items_to_move = ['grass', 'razor', 'guitar']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Put the rain and the tiger and the oven into Box 0.
boxes[0].append('rain')
boxes[0].append('tiger')
boxes[0].append('oven')

# Replace the spoon with the swimsuit in Box 1.
boxes[1].remove('spoon')
boxes[1].append('swimsuit')

# Put the watch into Box 2.
boxes[2].append('watch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")