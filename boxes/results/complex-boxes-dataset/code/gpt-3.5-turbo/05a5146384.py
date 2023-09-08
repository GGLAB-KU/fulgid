# Initial state of boxes
boxes = {
    0: ['leaf', 'fridge', 'mixer'],
    1: ['shelf', 'snow'],
    2: ['bowl'],
    3: ['violin', 'crown', 'submarine', 'table', 'flower'],
    4: ['horse', 'controller', 'bear'],
    5: ['umbrella', 'whistle', 'ring', 'coral', 'puzzle']
}

# Remove the coral from Box 5.
boxes[5].remove('coral')

# Remove the submarine from Box 3.
boxes[3].remove('submarine')

# Move the violin and the crown and the flower from Box 3 to Box 4.
items_to_move = ['violin', 'crown', 'flower']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Swap the mixer in Box 0 with the puzzle in Box 5.
boxes[0].remove('mixer')
boxes[5].remove('puzzle')
boxes[0].append('puzzle')
boxes[5].append('mixer')

# Put the magnet and the watch and the seaweed into Box 1.
items_to_put = ['magnet', 'watch', 'seaweed']
for item in items_to_put:
    boxes[1].append(item)

# Remove the table from Box 3.
boxes[3].remove('table')

# Remove the whistle from Box 5.
boxes[5].remove('whistle')

# Remove the fridge and the puzzle and the leaf from Box 0.
items_to_remove = ['fridge', 'puzzle', 'leaf']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the bowl in Box 2 with the violin in Box 4.
boxes[2].remove('bowl')
boxes[4].remove('violin')
boxes[2].append('violin')
boxes[4].append('bowl')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")