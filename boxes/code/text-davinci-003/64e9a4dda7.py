# Initialize the boxes
boxes = {
    0: [],
    1: ['boat', 'jacket'],
    2: ['apple'],
    3: [],
    4: ['bottle', 'pot'],
    5: ['bell'],
    6: ['ball', 'picture', 'shoe'],
}

# Define the moves
moves = [
    (5, 2, 'bell'),         # Move the bell from Box 5 to Box 2
    (4, 3, 'bottle'),       # Move the bottle from Box 4 to Box 3
    (4, 3, 'pot'),          # Move the pot from Box 4 to Box 3
    (None, 4, 'dress'),     # Put the dress into Box 4
    (None, 4, 'meat'),      # Put the meat into Box 4
    (None, 4, 'mirror'),    # Put the mirror into Box 4
    (2, None, 'apple'),     # Remove the apple from Box 2
    (2, None, 'bell'),      # Remove the bell from Box 2
    (None, 5, 'string'),    # Put the string into Box 5
    (None, 2, 'pipe'),      # Put the pipe into Box 2
    (None, 2, 'plate'),     # Put the plate into Box 2
    (1, 3, 'jacket'),       # Move the jacket from Box 1 to Box 3
    (3, 1, 'bottle'),       # Move the bottle from Box 3 to Box 1
    (4, None, 'dress'),     # Remove the dress from Box 4
    (4, None, 'mirror'),    # Remove the mirror from Box 4
    (6, None, 'ball'),      # Remove the ball from Box 6
    (6, None, 'shoe'),      # Remove the shoe from Box 6
    (5, None, 'string')     # Remove the string from Box 5
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