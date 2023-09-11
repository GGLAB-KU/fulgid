# Initial state of boxes
boxes = {
    0: [],
    1: ['branch', 'telescope', 'lion', 'lightning'],
    2: ['harmonica', 'tie', 'note', 'shampoo'],
    3: ['puzzle', 'mask', 'lamp'],
    4: ['cup']
}

# Remove the cup from Box 4.
boxes[4].remove('cup')

# Remove the branch from Box 1.
boxes[1].remove('branch')

# Replace the lion and the lightning and the telescope with the scissors and the shelf and the scarf in Box 1.
boxes[1].remove('lion')
boxes[1].remove('lightning')
boxes[1].remove('telescope')
boxes[1].append('scissors')
boxes[1].append('shelf')
boxes[1].append('scarf')

# Replace the harmonica and the tie with the earring and the octopus in Box 2.
boxes[2].remove('harmonica')
boxes[2].remove('tie')
boxes[2].append('earring')
boxes[2].append('octopus')

# Move the shampoo and the earring and the octopus from Box 2 to Box 3.
items_to_move = ['shampoo', 'earring', 'octopus']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Move the lamp and the earring from Box 3 to Box 1.
items_to_move = ['lamp', 'earring']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Remove the octopus from Box 3.
boxes[3].remove('octopus')

# Replace the shampoo with the violin in Box 3.
boxes[3].remove('shampoo')
boxes[3].append('violin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")