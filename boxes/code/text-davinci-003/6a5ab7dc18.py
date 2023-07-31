# Initialize the boxes
boxes = {
    0: ['magazine', 'suit', 'television'],
    1: ['train'],
    2: ['pot'],
    3: [],
    4: ['apple', 'milk'],
    5: ['cigarette', 'letter'],
    6: ['coat', 'sheet'],
}

# Define the moves
moves = [
    (0, None, 'magazine'),    # Remove the magazine from Box 0
    (0, None, 'television'),  # Remove the television from Box 0
    (2, None, 'pot'),         # Remove the pot from Box 2
    (4, None, 'apple'),       # Remove the apple from Box 4
    (5, None, 'letter'),      # Remove the letter from Box 5
    (None, 6, 'camera'),      # Put the camera into Box 6
    (None, 2, 'picture'),     # Put the picture into Box 2
    (6, None, 'camera'),      # Remove the camera from Box 6
    (6, None, 'sheet'),       # Remove the sheet from Box 6
    (6, 5, 'coat'),           # Move the coat from Box 6 to Box 5
    (0, 3, 'suit'),           # Move the suit from Box 0 to Box 3
    (2, 4, 'picture'),        # Move the picture from Box 2 to Box 4
    (None, 3, 'boot'),        # Put the boot into Box 3
    (None, 4, 'wire')         # Put the wire into Box 4
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