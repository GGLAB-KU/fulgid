# Initialize the boxes
boxes = {
    0: ['rock', 'wire'],
    1: ['map'],
    2: ['brick', 'ice'],
    3: ['hat'],
    4: ['coat', 'disk'],
    5: ['rose'],
    6: [],
}

# Define the moves
moves = [
    (None, 6, 'clock'),    # Put the clock into Box 6
    (None, 6, 'plane'),    # Put the plane into Box 6
    (0, 6, 'rock'),        # Move the rock from Box 0 to Box 6
    (5, None, 'rose'),     # Remove the rose from Box 5
    (None, 5, 'pot'),      # Put the pot into Box 5
    (1, None, 'map'),      # Remove the map from Box 1
    (5, None, 'pot'),      # Remove the pot from Box 5
    (4, 5, 'coat'),        # Move the coat from Box 4 to Box 5
    (4, 5, 'disk'),        # Move the disk from Box 4 to Box 5
    (2, 0, 'brick'),       # Move the brick from Box 2 to Box 0
    (2, 0, 'ice'),         # Move the ice from Box 2 to Box 0
    (None, 3, 'brain'),    # Put the brain into Box 3
    (None, 3, 'gift'),     # Put the gift into Box 3
    (0, None, 'ice'),      # Remove the ice from Box 0
    (0, None, 'wire'),     # Remove the wire from Box 0
    (5, None, 'disk'),     # Remove the disk from Box 5
    (3, 5, 'hat'),         # Move the hat from Box 3 to Box 5
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