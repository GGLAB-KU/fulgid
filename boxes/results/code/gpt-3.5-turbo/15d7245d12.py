# Initialize the boxes
boxes = {
    0: ['bottle', 'chemical'],
    1: ['paper', 'pipe'],
    2: ['rock', 'watch'],
    3: ['book', 'camera', 'wheel'],
    4: ['key', 'plane', 'radio'],
    5: ['cheese'],
    6: ['flower', 'seed', 'tissue'],
}

# Define the moves
moves = [
    (0, None, 'bottle'),       # Remove the bottle from Box 0
    (0, None, 'chemical'),     # Remove the chemical from Box 0
    (None, 5, 'bottle'),       # Put the bottle into Box 5
    (None, 5, 'magazine'),     # Put the magazine into Box 5
    (5, None, 'bottle'),       # Remove the bottle from Box 5
    (5, None, 'cheese'),       # Remove the cheese from Box 5
    (5, None, 'magazine'),     # Remove the magazine from Box 5
    (1, 5, 'paper'),           # Move the paper from Box 1 to Box 5
    (6, None, 'flower'),       # Remove the flower from Box 6
    (5, 2, 'paper'),           # Move the paper from Box 5 to Box 2
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