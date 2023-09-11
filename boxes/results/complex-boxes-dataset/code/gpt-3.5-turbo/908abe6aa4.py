# Initial state of boxes
boxes = {
    0: ['dolphin', 'bracelet', 'beach', 'note', 'charger'],
    1: ['controller', 'cat'],
    2: ['rocket', 'table', 'piano'],
    3: ['thunder', 'coin']
}

# Replace the beach with the shark in Box 0.
boxes[0].remove('beach')
boxes[0].append('shark')

# Remove the bracelet from Box 0.
boxes[0].remove('bracelet')

# Replace the table and the rocket with the shampoo and the earring in Box 2.
boxes[2].remove('table')
boxes[2].remove('rocket')
boxes[2].append('shampoo')
boxes[2].append('earring')

# Put the flower into Box 1.
boxes[1].append('flower')

# Remove the earring from Box 2.
boxes[2].remove('earring')

# Remove the cat and the controller and the flower from Box 1.
boxes[1].remove('cat')
boxes[1].remove('controller')
boxes[1].remove('flower')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")