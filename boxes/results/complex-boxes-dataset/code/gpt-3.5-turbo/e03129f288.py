# Initial state of boxes
boxes = {
    0: ['clock', 'telescope', 'cloud', 'coat', 'tie'],
    1: ['dice'],
    2: ['pot', 'fish', 'soap', 'camera', 'octopus'],
    3: [],
    4: [],
    5: ['plane']
}

# Remove the fish and the pot and the camera from Box 2.
items_to_remove = ['fish', 'pot', 'camera']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the clock and the tie from Box 0.
items_to_remove = ['clock', 'tie']
for item in items_to_remove:
    boxes[0].remove(item)

# Remove the coat from Box 0.
boxes[0].remove('coat')

# Swap the soap in Box 2 with the plane in Box 5.
boxes[2].remove('soap')
boxes[5].remove('plane')
boxes[2].append('plane')
boxes[5].append('soap')

# Swap the soap in Box 5 with the plane in Box 2.
boxes[5].remove('soap')
boxes[2].remove('plane')
boxes[5].append('plane')
boxes[2].append('soap')

# Swap the telescope in Box 0 with the dice in Box 1.
boxes[0].remove('telescope')
boxes[1].remove('dice')
boxes[0].append('dice')
boxes[1].append('telescope')

# Move the telescope from Box 1 to Box 5.
boxes[1].remove('telescope')
boxes[5].append('telescope')

# Move the dice and the cloud from Box 0 to Box 4.
items_to_move = ['dice', 'cloud']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Move the plane from Box 5 to Box 2.
boxes[5].remove('plane')
boxes[2].append('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")