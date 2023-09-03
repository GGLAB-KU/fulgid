# Initialize the boxes
boxes = {
    0: ['picture'],
    1: ['beer', 'coat', 'wheel'],
    2: ['brick', 'drug', 'flower'],
    3: [],
    4: ['bottle', 'leaf', 'pot'],
    5: ['game', 'newspaper'],
    6: ['bomb', 'string', 'tape'],
}

# Define the moves
moves = [
    (0, None, 'picture'),    # Remove the picture from Box 0
    (None, 3, 'bell'),        # Put the bell into Box 3
    (None, 3, 'watch'),       # Put the watch into Box 3
    (5, None, 'newspaper'),   # Remove the newspaper from Box 5
    (2, None, 'brick'),       # Remove the brick from Box 2
    (2, None, 'drug'),        # Remove the drug from Box 2
    (0, None, 'computer'),    # Put the computer into Box 0
    (6, None, 'string'),      # Remove the string from Box 6
    (6, None, 'pipe'),        # Put the pipe into Box 6
    (0, None, 'computer'),    # Remove the computer from Box 0
    (None, 3, 'plant'),       # Put the plant into Box 3
    (3, None, 'plant'),       # Remove the plant from Box 3
    (6, None, 'bomb'),        # Remove the bomb from Box 6
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