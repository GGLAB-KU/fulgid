# Initial state of boxes
boxes = {
    0: ['shelf'],
    1: ['grass', 'tree', 'controller'],
    2: [],
    3: [],
    4: ['note', 'laptop', 'shark', 'rain'],
    5: [],
    6: [],
    7: [],
    8: ['guitar'],
    9: [],
    10: ['helmet', 'pan', 'polish', 'frame', 'ocean'],
    11: ['flute', 'blanket', 'butterfly', 'submarine']
}

# Replace the guitar with the cow in Box 8.
boxes[8].remove('guitar')
boxes[8].append('cow')

# Swap the polish in Box 10 with the tree in Box 1.
boxes[10].remove('polish')
boxes[1].remove('tree')
boxes[10].append('tree')
boxes[1].append('polish')

# Replace the rain with the doll in Box 4.
boxes[4].remove('rain')
boxes[4].append('doll')

# Swap the controller in Box 1 with the shelf in Box 0.
boxes[1].remove('controller')
boxes[0].remove('shelf')
boxes[1].append('shelf')
boxes[0].append('controller')

# Remove the grass from Box 1.
boxes[1].remove('grass')

# Remove the note and the doll and the laptop from Box 4.
items_to_remove = ['note', 'doll', 'laptop']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the polish in Box 1 with the ocean in Box 10.
boxes[1].remove('polish')
boxes[10].remove('ocean')
boxes[1].append('ocean')
boxes[10].append('polish')

# Put the magnet and the planet into Box 3.
boxes[3].append('magnet')
boxes[3].append('planet')

# Put the sculpture and the frame and the lock into Box 2.
boxes[2].append('sculpture')
boxes[2].append('frame')
boxes[2].append('lock')

# Remove the pan from Box 10.
boxes[10].remove('pan')

# Move the controller from Box 0 to Box 6.
boxes[0].remove('controller')
boxes[6].append('controller')

# Swap the shark in Box 4 with the controller in Box 6.
boxes[4].remove('shark')
boxes[6].remove('controller')
boxes[4].append('controller')
boxes[6].append('shark')

# Replace the frame with the whistle in Box 10.
boxes[10].remove('frame')
boxes[10].append('whistle')

# Swap the controller in Box 4 with the cow in Box 8.
boxes[4].remove('controller')
boxes[8].remove('cow')
boxes[4].append('cow')
boxes[8].append('controller')

# Move the lock and the frame and the sculpture from Box 2 to Box 8.
items_to_move = ['lock', 'frame', 'sculpture']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[8].append(item)

# Replace the cow with the skirt in Box 4.
boxes[4].remove('cow')
boxes[4].append('skirt')

# Swap the skirt in Box 4 with the polish in Box 10.
boxes[4].remove('skirt')
boxes[10].remove('polish')
boxes[4].append('polish')
boxes[10].append('skirt')

# Replace the shelf with the mixer in Box 1.
boxes[1].remove('shelf')
boxes[1].append('mixer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")