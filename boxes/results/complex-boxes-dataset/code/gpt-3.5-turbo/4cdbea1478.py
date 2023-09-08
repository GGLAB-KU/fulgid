# Initial state of boxes
boxes = {
    0: [],
    1: ['coat', 'polish'],
    2: [],
    3: ['mask', 'planet', 'lipstick', 'horse', 'zipper'],
    4: ['flower', 'dice', 'table', 'grinder', 'clock']
}

# Remove the clock and the grinder and the table from Box 4.
items_to_remove = ['clock', 'grinder', 'table']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the lipstick and the zipper from Box 3 to Box 2.
items_to_move = ['lipstick', 'zipper']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Replace the flower and the dice with the skirt and the pants in Box 4.
boxes[4].remove('flower')
boxes[4].remove('dice')
boxes[4].append('skirt')
boxes[4].append('pants')

# Swap the polish in Box 1 with the pants in Box 4.
boxes[1].remove('polish')
boxes[4].remove('pants')
boxes[1].append('pants')
boxes[4].append('polish')

# Replace the polish and the skirt with the shark and the sculpture in Box 4.
boxes[4].remove('polish')
boxes[4].remove('skirt')
boxes[4].append('shark')
boxes[4].append('sculpture')

# Swap the coat in Box 1 with the zipper in Box 2.
boxes[1].remove('coat')
boxes[2].remove('zipper')
boxes[1].append('zipper')
boxes[2].append('coat')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")