# Initial state of boxes
boxes = {
    0: ['watch', 'blanket', 'lion'],
    1: ['lock', 'apple', 'battery', 'jungle'],
    2: ['dice', 'desert', 'bus', 'ocean', 'speaker'],
    3: ['telescope'],
    4: ['dress', 'plate'],
    5: ['toy', 'drum', 'chair', 'boat', 'sock'],
    6: ['pen', 'river', 'star', 'card'],
    7: [],
    8: ['phone', 'puzzle', 'cloud'],
    9: ['ship', 'rocket', 'belt'],
    10: ['button'],
    11: ['storm', 'toothpaste', 'toaster', 'branch', 'seaweed'],
    12: ['submarine', 'wig', 'shoe']
}

# Remove the telescope from Box 3.
boxes[3].remove('telescope')

# Move the shoe and the submarine from Box 12 to Box 11.
items_to_move = ['shoe', 'submarine']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[11].append(item)

# Remove the star from Box 6.
boxes[6].remove('star')

# Replace the cloud with the star in Box 8.
boxes[8].remove('cloud')
boxes[8].append('star')

# Put the grass into Box 11.
boxes[11].append('grass')

# Swap the wig in Box 12 with the battery in Box 1.
boxes[12].remove('wig')
boxes[1].remove('battery')
boxes[12].append('battery')
boxes[1].append('wig')

# Remove the card from Box 6.
boxes[6].remove('card')

# Swap the lock in Box 1 with the river in Box 6.
boxes[1].remove('lock')
boxes[6].remove('river')
boxes[1].append('river')
boxes[6].append('lock')

# Put the clock and the sculpture and the puzzle into Box 8.
items_to_move = ['clock', 'sculpture', 'puzzle']
for item in items_to_move:
    boxes[8].append(item)

# Move the battery from Box 12 to Box 0.
boxes[12].remove('battery')
boxes[0].append('battery')

# Put the rocket and the scissors and the ship into Box 7.
items_to_move = ['rocket', 'scissors', 'ship']
for item in items_to_move:
    boxes[7].append(item)

# Remove the sculpture from Box 8.
boxes[8].remove('sculpture')

# Move the plate and the dress from Box 4 to Box 9.
items_to_move = ['plate', 'dress']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[9].append(item)

# Move the button from Box 10 to Box 3.
boxes[10].remove('button')
boxes[3].append('button')

# Move the ship and the rocket from Box 9 to Box 7.
items_to_move = ['ship', 'rocket']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[7].append(item)

# Put the key and the bus and the planet into Box 9.
items_to_move = ['key', 'bus', 'planet']
for item in items_to_move:
    boxes[9].append(item)

# Move the lock and the pen from Box 6 to Box 3.
items_to_move = ['lock', 'pen']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Move the ship and the rocket from Box 7 to Box 6.
items_to_move = ['ship', 'rocket']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Put the towel into Box 0.
boxes[0].append('towel')

# Remove the belt and the planet and the bus from Box 9.
items_to_remove = ['belt', 'planet', 'bus']
for item in items_to_remove:
    boxes[9].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")