box = {
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

# Replace the guitar with the cow in Box 8
box[8] = ['cow']

# Swap the polish in Box 10 with the tree in Box 1
box[1].remove('tree')
box[10].append('tree')

# Replace the rain with the doll in Box 4
box[4].remove('rain')
box[4].append('doll')

# Swap the controller in Box 1 with the shelf in Box 0
box[0].append('controller')
box[1].remove('controller')

# Remove the grass from Box 1
box[1].remove('grass')

# Remove the note and the doll and the laptop from Box 4
box[4].remove('note')
box[4].remove('doll')
box[4].remove('laptop')

# Swap the polish in Box 1 with the ocean in Box 10
box[1].remove('polish')
box[10].append('polish')

# Put the magnet and the planet into Box 3
box[3] = ['magnet', 'planet']

# Put the sculpture and the frame and the lock into Box 2
box[2] = ['sculpture', 'frame', 'lock']

# Remove the pan from Box 10
box[10].remove('pan')

# Move the controller from Box 0 to Box 6
box[6].append('controller')
box[0].remove('controller')

# Swap the shark in Box 4 with the controller in Box 6
box[4].remove('shark')
box[6].append('shark')

# Replace the frame with the whistle in Box 10
box[10].remove('frame')
box[10].append('whistle')

# Swap the controller in Box 4 with the cow in Box 8
box[8].remove('cow')
box[4].append('cow')

# Move the lock and the frame and the sculpture from Box 2 to Box 8
box[8].extend(['lock', 'frame', 'sculpture'])
box[2] = []

# Replace the cow with the skirt in Box 4
box[4].remove('cow')
box[4].append('skirt')

# Swap the skirt in Box 4 with the polish in Box 10
box[10].remove('polish')
box[4].append('polish')

# Replace the shelf with the mixer in Box 1
box[1].remove('shelf')
box[1].append('mixer')

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")