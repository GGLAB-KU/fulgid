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