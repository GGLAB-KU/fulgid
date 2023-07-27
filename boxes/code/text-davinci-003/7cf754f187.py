# Initialize the boxes
boxes = {
    0: ['rose'],
    1: ['document', 'sheet'],
    2: ['engine', 'painting'],
    3: ['bell'],
    4: ['ball', 'clock', 'seed'],
    5: ['cross', 'tape'],
    6: ['card', 'cash'],
}

# Define the moves
moves = [
    (3, 0, 'bell'),         # Move the bell from Box 3 to Box 0
    (None, 3, 'block'),     # Put the block into Box 3
    (None, 3, 'key'),       # Put the key into Box 3
    (2, 5, 'painting'),     # Move the painting from Box 2 to Box 5
    (2, None, 'engine'),    # Remove the engine from Box 2
    (4, None, 'ball'),      # Remove the ball from Box 4
    (4, None, 'clock'),     # Remove the clock from Box 4
    (4, None, 'seed'),      # Remove the seed from Box 4
    (6, 1, 'card'),         # Move the card from Box 6 to Box 1
    (6, None, 'cash'),      # Remove the cash from Box 6
    (None, 6, 'fig'),       # Put the fig into Box 6
    (None, 2, 'picture'),   # Put the picture into Box 2
    (None, 2, 'tissue')     # Put the tissue into Box 2
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