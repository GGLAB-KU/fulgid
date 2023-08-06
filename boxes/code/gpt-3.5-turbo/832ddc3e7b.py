# Initialize the boxes
boxes = {
    0: [],
    1: ['cup', 'leaf', 'tie'],
    2: ['dress', 'game'],
    3: ['brick', 'camera', 'file'],
    4: ['book'],
    5: ['cross'],
    6: ['map', 'stone'],
}

# Define the moves
moves = [
    (2, None, 'dress'),       # Remove the dress from Box 2
    (3, None, 'camera'),      # Remove the camera from Box 3
    (3, None, 'file'),        # Remove the file from Box 3
    (3, None, 'brick'),       # Remove the brick from Box 3
    (None, 5, 'brick'),       # Put the brick into Box 5
    (5, None, 'cross'),       # Remove the cross from Box 5
    (None, 2, 'block'),       # Put the block into Box 2
    (4, None, 'book'),        # Remove the book from Box 4
    (6, 4, 'stone'),          # Move the stone from Box 6 to Box 4
    (None, 2, 'creature'),    # Put the creature into Box 2
    (2, None, 'creature'),    # Remove the creature from Box 2
    (1, None, 'cup'),         # Remove the cup from Box 1
    (1, None, 'leaf'),        # Remove the leaf from Box 1
    (1, None, 'tie'),         # Remove the tie from Box 1
    (6, None, 'map')          # Remove the map from Box 6
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