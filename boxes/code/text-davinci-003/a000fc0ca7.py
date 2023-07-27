# Initialize the boxes
boxes = {
    0: ['bell', 'shirt'],
    1: [],
    2: ['coat'],
    3: [],
    4: ['ice', 'magazine', 'stone'],
    5: ['camera', 'tape'],
    6: ['map', 'mirror'],
}

# Define the moves
moves = [
    (4, None, 'ice'),       # Remove the ice from Box 4
    (4, None, 'magazine'),  # Remove the magazine from Box 4
    (4, 0, 'stone'),        # Move the stone from Box 4 to Box 0
    (2, 1, 'coat'),         # Move the coat from Box 2 to Box 1
    (0, None, 'bell'),      # Remove the bell from Box 0
    (0, None, 'shirt'),     # Remove the shirt from Box 0
    (5, 0, 'camera'),       # Move the camera from Box 5 to Box 0
    (5, 0, 'tape'),         # Move the tape from Box 5 to Box 0
    (None, 2, 'flower'),    # Put the flower into Box 2
    (2, None, 'flower'),    # Remove the flower from Box 2
    (0, None, 'camera'),    # Remove the camera from Box 0
    (None, 4, 'cash'),      # Put the cash into Box 4
    (None, 4, 'wire'),      # Put the wire into Box 4
    (6, 3, 'map'),          # Move the map from Box 6 to Box 3
    (None, 5, 'branch'),    # Put the branch into Box 5
    (0, None, 'bomb'),      # Put the bomb into Box 0
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