# Initialize the boxes
boxes = {
    0: ['fig'],
    1: ['newspaper', 'tape'],
    2: ['bread', 'shirt'],
    3: ['bus', 'hat', 'rose'],
    4: ['bag', 'boat', 'suit'],
    5: ['plane', 'string'],
    6: ['coat', 'magazine'],
}

# Define the moves
moves = [
    (4, 5, 'bag'),       # Move the bag from Box 4 to Box 5
    (None, 4, 'bowl'),   # Put the bowl into Box 4
    (None, 6, 'picture'),# Put the picture into Box 6
    (None, 2, 'gift'),   # Put the gift into Box 2
    (3, None, 'bus'),    # Remove the bus from Box 3
    (1, None, 'tape'),   # Remove the tape from Box 1
    (3, None, 'hat'),    # Remove the hat from Box 3
    (None, 1, 'bus'),    # Put the bus into Box 1
    (1, None, 'newspaper'),  # Remove the newspaper from Box 1
    (3, None, 'rose')    # Remove the rose from Box 3
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