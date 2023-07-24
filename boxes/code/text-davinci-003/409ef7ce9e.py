# Initialize the boxes
boxes = {
    0: [],
    1: ['apple', 'bell', 'pipe'],
    2: [],
    3: [],
    4: ['key'],
    5: [],
    6: ['rose'],
}

# Define the moves
moves = [
    (4, None, 'key'),       # Remove the key from Box 4
    (None, 3, 'crown'),     # Put the crown into Box 3
    (None, 3, 'seed'),      # Put the seed into Box 3
    (None, 0, 'bowl'),      # Put the bowl into Box 0
    (None, 0, 'drug'),      # Put the drug into Box 0
    (6, 5, 'rose'),         # Move the rose from Box 6 to Box 5
    (0, 4, 'bowl'),         # Move the bowl from Box 0 to Box 4
    (0, 4, 'drug'),         # Move the drug from Box 0 to Box 4
    (1, None, 'pipe'),      # Remove the pipe from Box 1
    (1, None, 'bell'),      # Remove the bell from Box 1
    (5, None, 'rose'),      # Remove the rose from Box 5
    (4, None, 'bowl'),      # Remove the bowl from Box 4
    (None, 1, 'cake'),      # Put the cake into Box 1
    (None, 1, 'rose')       # Put the rose into Box 1
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