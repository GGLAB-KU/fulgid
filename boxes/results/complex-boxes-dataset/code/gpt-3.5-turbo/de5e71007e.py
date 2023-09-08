# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['button', 'magnet'],
    3: ['puzzle', 'tie'],
    4: [],
    5: ['plate'],
    6: []
}

# Put the elephant and the dice and the thread into Box 5.
items_to_move = ['elephant', 'dice', 'thread']
for item in items_to_move:
    boxes[5].append(item)

# Swap the button in Box 2 with the puzzle in Box 3.
boxes[2].remove('button')
boxes[3].remove('puzzle')
boxes[2].append('puzzle')
boxes[3].append('button')

# Empty Box 5.
boxes[5] = []

# Move the button and the tie from Box 3 to Box 0.
items_to_move = ['button', 'tie']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Swap the puzzle in Box 2 with the tie in Box 0.
boxes[2].remove('puzzle')
boxes[0].remove('tie')
boxes[2].append('tie')
boxes[0].append('puzzle')

# Swap the magnet in Box 2 with the puzzle in Box 0.
boxes[2].remove('magnet')
boxes[0].remove('puzzle')
boxes[2].append('puzzle')
boxes[0].append('magnet')

# Move the button and the magnet from Box 0 to Box 3.
items_to_move = ['button', 'magnet']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Swap the tie in Box 2 with the magnet in Box 3.
boxes[2].remove('tie')
boxes[3].remove('magnet')
boxes[2].append('magnet')
boxes[3].append('tie')

# Put the scarf and the elephant into Box 1.
items_to_move = ['scarf', 'elephant']
for item in items_to_move:
    boxes[1].append(item)

# Remove the button from Box 3.
boxes[3].remove('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")