# Initial state of boxes
boxes = {
    0: ['guitar', 'keyboard'],
    1: ['meteor', 'key', 'toothbrush', 'needle', 'moon'],
    2: ['lipstick', 'motorcycle', 'island', 'phone', 'razor'],
    3: ['earring', 'magnet'],
    4: ['coat', 'drum', 'button'],
    5: [],
    6: ['mountain', 'pillow', 'bowl'],
    7: ['cat', 'table'],
    8: []
}

# Remove the magnet from Box 3.
boxes[3].remove('magnet')

# Swap the guitar in Box 0 with the pillow in Box 6.
boxes[0].remove('guitar')
boxes[6].remove('pillow')
boxes[0].append('pillow')
boxes[6].append('guitar')

# Move the earring from Box 3 to Box 1.
boxes[3].remove('earring')
boxes[1].append('earring')

# Remove the button from Box 4.
boxes[4].remove('button')

# Replace the mountain and the bowl with the tree and the violin in Box 6.
boxes[6].remove('mountain')
boxes[6].remove('bowl')
boxes[6].append('tree')
boxes[6].append('violin')

# Remove the keyboard and the pillow from Box 0.
boxes[0].remove('keyboard')
boxes[0].remove('pillow')

# Replace the drum with the coin in Box 4.
boxes[4].remove('drum')
boxes[4].append('coin')

# Put the sandals and the train into Box 7.
boxes[7].append('sandals')
boxes[7].append('train')

# Put the horse into Box 1.
boxes[1].append('horse')

# Remove the guitar from Box 6.
boxes[6].remove('guitar')

# Replace the razor and the lipstick with the headphone and the cat in Box 2.
boxes[2].remove('razor')
boxes[2].remove('lipstick')
boxes[2].append('headphone')
boxes[2].append('cat')

# Move the table from Box 7 to Box 1.
boxes[7].remove('table')
boxes[1].append('table')

# Move the coat and the coin from Box 4 to Box 1.
boxes[4].remove('coat')
boxes[4].remove('coin')
boxes[1].append('coat')
boxes[1].append('coin')

# Remove the tree from Box 6.
boxes[6].remove('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")