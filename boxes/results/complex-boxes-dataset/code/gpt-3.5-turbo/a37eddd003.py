# Initial state of boxes
boxes = {
    0: ['dice', 'microscope', 'horn', 'star'],
    1: ['polish', 'snow', 'jacket', 'starfish'],
    2: ['cat'],
    3: ['soap', 'elephant', 'tie', 'camera', 'shoe'],
    4: ['glasses', 'lipstick', 'bicycle', 'oven'],
    5: ['butterfly', 'toothpaste', 'battery', 'console', 'lion'],
    6: ['button', 'boot', 'bus'],
    7: [],
    8: ['bracelet', 'pen'],
    9: []
}

# Put the bracelet into Box 6.
boxes[6].append('bracelet')

# Put the shark and the pan into Box 4.
boxes[4].append('shark')
boxes[4].append('pan')

# Empty Box 3.
boxes[3] = []

# Move the console and the battery from Box 5 to Box 4.
items_to_move = ['console', 'battery']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Replace the cat with the tie in Box 2.
boxes[2].remove('cat')
boxes[2].append('tie')

# Swap the pen in Box 8 with the horn in Box 0.
boxes[8].remove('pen')
boxes[0].remove('horn')
boxes[8].append('horn')
boxes[0].append('pen')

# Replace the polish with the book in Box 1.
boxes[1].remove('polish')
boxes[1].append('book')

# Swap the tie in Box 2 with the bus in Box 6.
boxes[2].remove('tie')
boxes[6].remove('bus')
boxes[2].append('bus')
boxes[6].append('tie')

# Move the horn and the bracelet from Box 8 to Box 6.
items_to_move = ['horn', 'bracelet']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Move the bus from Box 2 to Box 0.
boxes[2].remove('bus')
boxes[0].append('bus')

# Remove the oven and the bicycle and the shark from Box 4.
items_to_remove = ['oven', 'bicycle', 'shark']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the console in Box 4 with the toothpaste in Box 5.
boxes[4].remove('console')
boxes[5].remove('toothpaste')
boxes[4].append('toothpaste')
boxes[5].append('console')

# Put the pants into Box 2.
boxes[2].append('pants')

# Put the glasses and the lock into Box 9.
boxes[9].append('glasses')
boxes[9].append('lock')

# Remove the pants from Box 2.
boxes[2].remove('pants')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")