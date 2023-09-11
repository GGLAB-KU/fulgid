# Initial state of boxes
boxes = {
    0: ['camera', 'speaker', 'candle', 'drum'],
    1: ['forest', 'tape'],
    2: [],
    3: ['lightning', 'harmonica'],
    4: ['polish', 'lion', 'game', 'comb']
}

# Put the lion into Box 3.
boxes[3].append('lion')

# Put the shirt into Box 1.
boxes[1].append('shirt')

# Remove the candle and the camera and the drum from Box 0.
items_to_remove = ['candle', 'camera', 'drum']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the lion and the harmonica with the console and the tree in Box 3.
boxes[3].remove('lion')
boxes[3].remove('harmonica')
boxes[3].append('console')
boxes[3].append('tree')

# Move the lion and the game and the polish from Box 4 to Box 1.
items_to_move = ['lion', 'game', 'polish']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Put the tie into Box 0.
boxes[0].append('tie')

# Move the tie from Box 0 to Box 4.
boxes[0].remove('tie')
boxes[4].append('tie')

# Replace the tie and the comb with the coat and the charger in Box 4.
boxes[4].remove('tie')
boxes[4].remove('comb')
boxes[4].append('coat')
boxes[4].append('charger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")