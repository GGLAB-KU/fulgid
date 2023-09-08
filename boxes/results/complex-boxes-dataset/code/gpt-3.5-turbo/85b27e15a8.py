# Initial state of boxes
boxes = {
    0: ['polish', 'shirt'],
    1: ['tree', 'pen', 'apple', 'bell'],
    2: ['seaweed', 'wire'],
    3: ['gloves', 'mask'],
    4: ['button', 'planet', 'dice', 'lock', 'necklace'],
    5: ['sandals', 'chair', 'wallet']
}

# Remove the necklace and the button and the dice from Box 4.
items_to_remove = ['necklace', 'button', 'dice']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the bell and the tree from Box 1 to Box 0.
items_to_move = ['bell', 'tree']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Remove the lock and the planet from Box 4.
items_to_remove = ['lock', 'planet']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the beach and the bicycle into Box 2.
items_to_add = ['beach', 'bicycle']
for item in items_to_add:
    boxes[2].append(item)

# Move the polish from Box 0 to Box 4.
boxes[0].remove('polish')
boxes[4].append('polish')

# Remove the apple from Box 1.
boxes[1].remove('apple')

# Remove the sandals from Box 5.
boxes[5].remove('sandals')

# Empty Box 5.
boxes[5] = []

# Move the seaweed and the beach and the wire from Box 2 to Box 1.
items_to_move = ['seaweed', 'beach', 'wire']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")