# Initialize the boxes
boxes = {
    0: ['bottle', 'document'],
    1: ['key'],
    2: ['cake'],
    3: ['ball', 'crown'],
    4: ['bell', 'computer'],
    5: ['game'],
    6: [],
}

# Define the moves
moves = [
    (5, 6, 'game'),         # Move the game from Box 5 to Box 6
    (None, 4, 'fan'),       # Put the fan into Box 4
    (2, None, 'cake'),      # Remove the cake from Box 2
    (4, 1, 'bell'),         # Move the bell from Box 4 to Box 1
    (4, 1, 'computer'),     # Move the computer from Box 4 to Box 1
    (3, 4, 'ball'),         # Move the ball from Box 3 to Box 4
    (None, 2, 'shell'),     # Put the shell into Box 2
    (None, 3, 'chemical'),  # Put the chemical into Box 3
    (6, 4, 'game'),         # Move the game from Box 6 to Box 4
    (0, None, 'bottle'),    # Remove the bottle from Box 0
    (0, None, 'document'),  # Remove the document from Box 0
    (4, None, 'game')       # Remove the game from Box 4
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