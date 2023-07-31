# Initialize the boxes
boxes = {
    0: ['gift'],
    1: ['ball', 'bone', 'sheet'],
    2: ['game', 'map', 'tissue'],
    3: [],
    4: ['document'],
    5: ['key'],
    6: ['bomb', 'machine', 'picture'],
}

# Define the moves
moves = [
    (5, 0, 'key'),          # Move the key from Box 5 to Box 0
    (None, 3, 'medicine'),  # Put the medicine into Box 3
    (None, 3, 'tie'),       # Put the tie into Box 3
    (6, None, 'machine'),   # Remove the machine from Box 6
    (6, None, 'picture'),   # Remove the picture from Box 6
    (1, None, 'bone'),      # Remove the bone from Box 1
    (2, None, 'tissue'),    # Remove the tissue from Box 2
    (None, 3, 'fish'),      # Put the fish into Box 3
    (3, None, 'medicine'),  # Remove the medicine from Box 3
    (2, 1, 'map'),          # Move the map from Box 2 to Box 1
    (None, 0, 'brick'),     # Put the brick into Box 0
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