# Initialize the boxes
boxes = {
    0: ['pot', 'suit', 'ticket'],
    1: ['cake', 'string', 'wire'],
    2: ['bus', 'document'],
    3: ['bell', 'cigarette', 'mirror'],
    4: [],
    5: ['cup'],
    6: ['leaf'],
}

# Define the moves
moves = [
    (0, 2, 'pot'),          # Move the pot from Box 0 to Box 2
    (5, 4, 'cup'),          # Move the cup from Box 5 to Box 4
    (6, 0, 'leaf'),         # Move the leaf from Box 6 to Box 0
    (1, None, 'cake'),      # Remove the cake from Box 1
    (1, None, 'wire'),      # Remove the wire from Box 1
    (None, 4, 'map'),       # Put the map into Box 4
    (None, 4, 'camera'),    # Put the camera into Box 4
    (1, 5, 'string'),       # Move the string from Box 1 to Box 5
    (None, 5, 'newspaper'), # Put the newspaper into Box 5
    (0, None, 'suit'),      # Remove the suit from Box 0
    (3, None, 'bell'),      # Remove the bell from Box 3
    (3, None, 'mirror'),    # Remove the mirror from Box 3
    (0, None, 'ticket'),    # Remove the ticket from Box 0
    (0, None, 'leaf'),      # Remove the leaf from Box 0
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