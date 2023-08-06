# Initialize the boxes
boxes = {
    0: ['guitar', 'picture'],
    1: [],
    2: ['branch', 'flower', 'painting'],
    3: ['seed'],
    4: ['boot', 'ring'],
    5: ['cake', 'document'],
    6: ['dress'],
}

# Define the moves
moves = [
    (2, 4, 'flower'),       # Move the flower from Box 2 to Box 4
    (6, None, 'dress'),     # Remove the dress from Box 6
    (3, 2, 'seed'),         # Move the seed from Box 3 to Box 2
    (4, 6, 'boot'),         # Move the boot from Box 4 to Box 6
    (4, 1, 'ring'),         # Move the ring from Box 4 to Box 1
    (4, None, 'flower'),    # Remove the flower from Box 4
    (1, None, 'ring'),      # Remove the ring from Box 1
    (0, 3, 'guitar'),       # Move the guitar from Box 0 to Box 3
    (0, 3, 'picture'),      # Move the picture from Box 0 to Box 3
    (3, None, 'picture'),   # Remove the picture from Box 3
    (None, 0, 'bell'),      # Put the bell into Box 0
    (None, 0, 'tie'),       # Put the tie into Box 0
    (6, None, 'boot')       # Remove the boot from Box 6
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