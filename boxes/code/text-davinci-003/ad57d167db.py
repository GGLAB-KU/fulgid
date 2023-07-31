# Initialize the boxes
boxes = {
    0: ['file'],
    1: ['bell', 'newspaper', 'paper'],
    2: ['document', 'fan'],
    3: ['beer', 'train'],
    4: ['engine', 'flower', 'game'],
    5: [],
    6: ['drink'],
}

# Define the moves
moves = [
    (0, None, 'file'),       # Remove the file from Box 0
    (4, None, 'engine'),     # Remove the engine from Box 4
    (None, 4, 'bread'),      # Put the bread into Box 4
    (4, None, 'bread'),      # Remove the bread from Box 4
    (6, 5, 'drink'),         # Move the drink from Box 6 to Box 5
    (2, 0, 'fan'),           # Move the fan from Box 2 to Box 0
    (4, None, 'flower'),     # Remove the flower from Box 4
    (4, 6, 'game'),          # Move the game from Box 4 to Box 6
    (2, None, 'document'),   # Remove the document from Box 2
    (1, None, 'bell'),       # Remove the bell from Box 1
    (1, None, 'newspaper'),  # Remove the newspaper from Box 1
    (1, None, 'paper'),      # Remove the paper from Box 1
    (None, 6, 'bill')        # Put the bill into Box 6
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