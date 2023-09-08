# Initial state of boxes
boxes = {
    0: ['chair', 'paint', 'candle'],
    1: [],
    2: ['sock'],
    3: ['guitar', 'mask'],
    4: ['book', 'pot', 'makeup', 'cup'],
    5: ['doll', 'polish', 'comet', 'tiger'],
    6: ['forest', 'cloud', 'tie'],
    7: ['lipstick'],
    8: []
}

# Remove the tie and the cloud and the forest from Box 6.
items_to_remove = ['tie', 'cloud', 'forest']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the candle and the chair from Box 0 to Box 5.
items_to_move = ['candle', 'chair']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Move the paint from Box 0 to Box 3.
boxes[0].remove('paint')
boxes[3].append('paint')

# Move the sock from Box 2 to Box 3.
boxes[2].remove('sock')
boxes[3].append('sock')

# Swap the polish in Box 5 with the lipstick in Box 7.
boxes[5].remove('polish')
boxes[7].remove('lipstick')
boxes[5].append('lipstick')
boxes[7].append('polish')

# Remove the sock and the guitar from Box 3.
boxes[3].remove('sock')
boxes[3].remove('guitar')

# Swap the makeup in Box 4 with the polish in Box 7.
boxes[4].remove('makeup')
boxes[7].remove('polish')
boxes[4].append('polish')
boxes[7].append('makeup')

# Swap the lipstick in Box 5 with the paint in Box 3.
boxes[5].remove('lipstick')
boxes[3].remove('paint')
boxes[5].append('paint')
boxes[3].append('lipstick')

# Replace the mask with the lion in Box 3.
boxes[3].remove('mask')
boxes[3].append('lion')

# Replace the lipstick and the lion with the scarf and the chair in Box 3.
boxes[3].remove('lipstick')
boxes[3].remove('lion')
boxes[3].append('scarf')
boxes[3].append('chair')

# Remove the candle and the tiger and the paint from Box 5.
items_to_remove = ['candle', 'tiger', 'paint']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the comet and the chair from Box 5.
items_to_remove = ['comet', 'chair']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the chair from Box 3.
boxes[3].remove('chair')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")