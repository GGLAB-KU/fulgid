# Initialize the boxes
boxes = {
    0: [],
    1: ['computer'],
    2: ['leaf', 'picture', 'rose'],
    3: ['bus', 'hat'],
    4: ['dish'],
    5: ['guitar', 'jacket'],
    6: ['disk', 'seed'],
}

# Define the moves
moves = [
    (6, None, 'disk'),       # Remove the disk from Box 6
    (6, None, 'seed'),       # Remove the seed from Box 6
    (1, 6, 'computer'),      # Move the computer from Box 1 to Box 6
    (5, None, 'guitar'),     # Remove the guitar from Box 5
    (5, None, 'jacket'),     # Remove the jacket from Box 5
    (2, 0, 'picture'),       # Move the picture from Box 2 to Box 0
    (None, 5, 'bag'),        # Put the bag into Box 5
    (None, 5, 'radio')       # Put the radio into Box 5
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