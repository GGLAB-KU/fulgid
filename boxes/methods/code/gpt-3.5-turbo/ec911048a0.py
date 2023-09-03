# Initialize the boxes
boxes = {
    0: ['newspaper', 'painting'],
    1: ['bone', 'gift', 'stone'],
    2: ['cash', 'tissue'],
    3: ['hat', 'pot', 'tape'],
    4: [],
    5: ['bag'],
    6: ['bill', 'string'],
}

# Define the moves
moves = [
    (5, None, 'bag'),       # Remove the bag from Box 5
    (None, 4, 'beer'),      # Put the beer into Box 4
    (1, None, 'bone'),      # Remove the bone from Box 1
    (1, None, 'gift'),      # Remove the gift from Box 1
    (1, None, 'stone'),     # Remove the stone from Box 1
    (4, None, 'beer'),      # Remove the beer from Box 4
    (3, None, 'hat'),       # Remove the hat from Box 3
    (3, None, 'pot'),       # Remove the pot from Box 3
    (3, None, 'tape'),      # Remove the tape from Box 3
    (None, 0, 'camera'),    # Put the camera into Box 0
    (None, 4, 'fig'),       # Put the fig into Box 4
    (0, None, 'camera'),    # Remove the camera from Box 0
    (0, None, 'painting'),  # Remove the painting from Box 0
    (None, 3, 'cream'),     # Put the cream into Box 3
    (None, 3, 'ice'),       # Put the ice into Box 3
    (None, 3, 'wheel'),     # Put the wheel into Box 3
    (2, None, 'tissue'),    # Remove the tissue from Box 2
    (6, 1, 'bill'),         # Move the bill from Box 6 to Box 1
    (6, 1, 'string'),       # Move the string from Box 6 to Box 1
    (None, 0, 'bomb'),      # Put the bomb into Box 0
    (None, 0, 'watch')      # Put the watch into Box 0
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