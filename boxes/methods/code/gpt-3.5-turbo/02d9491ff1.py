# Initialize the boxes
boxes = {
    0: [],
    1: ['letter', 'shoe', 'train'],
    2: ['document'],
    3: ['bus'],
    4: ['cash', 'fish'],
    5: [],
    6: ['paper', 'stone'],
}

# Define the moves
moves = [
    (None, 3, 'camera'),       # Put the camera into Box 3
    (None, 3, 'chemical'),     # Put the chemical into Box 3
    (2, None, 'document'),     # Remove the document from Box 2
    (1, None, 'letter'),       # Remove the letter from Box 1
    (1, None, 'shoe'),         # Remove the shoe from Box 1
    (1, 6, 'train'),           # Move the train from Box 1 to Box 6
    (3, None, 'camera'),       # Remove the camera from Box 3
    (3, None, 'chemical'),     # Remove the chemical from Box 3
    (6, None, 'paper'),        # Remove the paper from Box 6
    (6, None, 'train'),        # Remove the train from Box 6
    (3, 6, 'bus'),             # Move the bus from Box 3 to Box 6
    (6, None, 'bus'),          # Remove the bus from Box 6
    (6, 0, 'stone'),           # Move the stone from Box 6 to Box 0
    (None, 6, 'game'),         # Put the game into Box 6
    (None, 6, 'picture'),      # Put the picture into Box 6
    (6, None, 'picture'),      # Remove the picture from Box 6
    (0, None, 'stone'),        # Remove the stone from Box 0
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