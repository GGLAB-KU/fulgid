# Initialize the boxes
boxes = {
    0: ['note'],
    1: [],
    2: ['ball'],
    3: [],
    4: ['bus', 'camera', 'radio'],
    5: ['cream', 'tie'],
    6: ['document'],
}

# Define the moves
moves = [
    (4, 1, 'bus'),          # Move the bus from Box 4 to Box 1
    (4, 1, 'camera'),       # Move the camera from Box 4 to Box 1
    (4, 1, 'radio'),        # Move the radio from Box 4 to Box 1
    (None, 0, 'mirror'),    # Put the mirror into Box 0
    (6, 0, 'document'),     # Move the document from Box 6 to Box 0
    (1, None, 'bus'),       # Remove the bus from Box 1
    (1, None, 'radio'),     # Remove the radio from Box 1
    (None, 6, 'bell'),      # Put the bell into Box 6
    (None, 6, 'jacket'),    # Put the jacket into Box 6
    (None, 3, 'plate'),     # Put the plate into Box 3
    (6, 4, 'jacket'),       # Move the jacket from Box 6 to Box 4
    (3, None, 'plate'),     # Remove the plate from Box 3
    (2, 1, 'ball'),         # Move the ball from Box 2 to Box 1
    (None, 5, 'bill'),      # Put the bill into Box 5
    (None, 2, 'computer'),  # Put the computer into Box 2
    (None, 1, 'ring')       # Put the ring into Box 1
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