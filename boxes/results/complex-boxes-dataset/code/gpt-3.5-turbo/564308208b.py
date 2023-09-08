# Initial state of boxes
boxes = {
    0: ['coat'],
    1: ['microscope', 'candle', 'tree', 'pillow', 'guitar'],
    2: ['horse', 'shark', 'magnet', 'mirror'],
    3: ['lipstick', 'star'],
    4: [],
    5: ['earring'],
    6: ['headphone', 'comet', 'polish', 'speaker', 'dog']
}

# Replace the coat with the plane in Box 0.
boxes[0].remove('coat')
boxes[0].append('plane')

# Replace the comet and the dog with the storm and the meteor in Box 6.
boxes[6].remove('comet')
boxes[6].remove('dog')
boxes[6].append('storm')
boxes[6].append('meteor')

# Move the headphone from Box 6 to Box 1.
boxes[6].remove('headphone')
boxes[1].append('headphone')

# Empty Box 3.
boxes[3] = []

# Put the pen into Box 0.
boxes[0].append('pen')

# Swap the guitar in Box 1 with the plane in Box 0.
boxes[1].remove('guitar')
boxes[0].remove('plane')
boxes[1].append('plane')
boxes[0].append('guitar')

# Move the storm and the meteor and the speaker from Box 6 to Box 2.
items_to_move = ['storm', 'meteor', 'speaker']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Swap the pen in Box 0 with the earring in Box 5.
boxes[0].remove('pen')
boxes[5].remove('earring')
boxes[0].append('earring')
boxes[5].append('pen')

# Move the guitar from Box 0 to Box 2.
boxes[0].remove('guitar')
boxes[2].append('guitar')

# Put the toothpaste and the mirror and the pants into Box 1.
items_to_move = ['toothpaste', 'mirror', 'pants']
for item in items_to_move:
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")