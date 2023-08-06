# Initialize the boxes
boxes = {
    0: ['plane', 'seed'],
    1: ['pipe'],
    2: ['engine', 'tissue'],
    3: ['picture', 'string'],
    4: ['bomb', 'cheese'],
    5: ['brick', 'tie'],
    6: ['flower', 'key'],
}

# Define the moves
moves = [
    (3, 1, 'string'),       # Move the string from Box 3 to Box 1
    (None, 3, 'tape'),      # Put the tape into Box 3
    (2, 4, 'engine'),       # Move the engine from Box 2 to Box 4
    (2, 3, 'tissue'),       # Move the tissue from Box 2 to Box 3
    (4, None, 'cheese'),    # Remove the cheese from Box 4
    (0, None, 'plane'),     # Remove the plane from Box 0
    (0, None, 'seed'),      # Remove the seed from Box 0
    (3, None, 'tape'),      # Remove the tape from Box 3
    (3, None, 'tissue'),    # Remove the tissue from Box 3
    (1, None, 'pipe'),      # Remove the pipe from Box 1
    (1, None, 'string')     # Remove the string from Box 1
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