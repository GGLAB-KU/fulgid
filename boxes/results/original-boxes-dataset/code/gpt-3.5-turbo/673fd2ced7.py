# Initialize the boxes
boxes = {
    0: ['cash', 'suit'],
    1: ['bell', 'medicine', 'shoe'],
    2: ['cake', 'clock', 'engine'],
    3: ['map', 'pot'],
    4: ['fan', 'mirror'],
    5: ['block', 'string', 'train'],
    6: ['disk'],
}

# Define the moves
moves = [
    (4, None, 'mirror'),    # Remove the mirror from Box 4
    (4, None, 'fan'),       # Remove the fan from Box 4
    (0, None, 'cash'),      # Remove the cash from Box 0
    (0, None, 'suit'),      # Remove the suit from Box 0
    (2, None, 'clock'),     # Remove the clock from Box 2
    (2, None, 'engine'),    # Remove the engine from Box 2
    (None, 4, 'camera'),    # Put the camera into Box 4
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