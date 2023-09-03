# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['meat'],
    3: ['fan'],
    4: ['bell'],
    5: ['map'],
    6: ['bottle', 'car', 'document'],
}

# Define the moves
moves = [
    (2, None, 'meat'),       # Remove the meat from Box 2
    (3, None, 'fan'),        # Remove the fan from Box 3
    (4, None, 'bell'),       # Remove the bell from Box 4
    (5, None, 'map'),        # Remove the map from Box 5
    (6, None, 'bottle'),     # Remove the bottle from Box 6
    (6, None, 'car'),        # Remove the car from Box 6
    (6, None, 'document'),   # Remove the document from Box 6
    (0, None, 'nothing'),    # Put nothing into Box 0
    (1, None, 'nothing'),    # Put nothing into Box 1
    (2, None, 'meat'),       # Put the meat into Box 2
    (3, None, 'fan'),        # Put the fan into Box 3
    (4, None, 'bell'),       # Put the bell into Box 4
    (5, None, 'map'),        # Put the map into Box 5
    (6, None, 'bottle'),     # Put the bottle into Box 6
    (6, None, 'car'),        # Put the car into Box 6
    (6, None, 'document')    # Put the document into Box 6
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