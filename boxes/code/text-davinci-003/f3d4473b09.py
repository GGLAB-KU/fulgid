# Initialize the boxes
boxes = {
    0: ['machine', 'medicine', 'tea'],
    1: ['magazine', 'phone'],
    2: ['bone', 'egg', 'file'],
    3: ['map', 'radio'],
    4: ['brain'],
    5: ['bell', 'meat'],
    6: ['card', 'cross'],
}

# Define the moves
moves = [
    (3, None, 'radio'),     # Remove the radio from Box 3
    (6, 4, 'card'),         # Move the card from Box 6 to Box 4
    (5, 4, 'meat'),         # Move the meat from Box 5 to Box 4
    (None, 6, 'flower'),    # Put the flower into Box 6
    (None, 3, 'boat'),      # Put the boat into Box 3
    (3, 1, 'boat'),         # Move the boat from Box 3 to Box 1
    (0, 3, 'tea'),          # Move the tea from Box 0 to Box 3
    (3, 5, 'map'),          # Move the map from Box 3 to Box 5
    (3, 5, 'tea'),          # Move the tea from Box 3 to Box 5
    (5, 3, 'bell'),         # Move the bell from Box 5 to Box 3
    (6, None, 'flower'),    # Remove the flower from Box 6
    (3, None, 'bell')       # Remove the bell from Box 3
]

# Execute the moves
for move in moves:
    src, dest, item = move

    if src is not None:  # If there's a source box, remove item from it
        boxes[src].remove(item)

    if dest is not None:  # If there's a destination box, add item to it
        boxes[dest].append(item)

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")