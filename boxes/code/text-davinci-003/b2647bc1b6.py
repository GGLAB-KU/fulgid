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
    (None, 5, 'radio'),      # Put the radio into Box 5
    (2, None, 'leaf'),       # Remove the leaf from Box 2
    (2, None, 'rose'),       # Remove the rose from Box 2
    (None, 1, 'cream'),      # Put the cream into Box 1
    (None, 0, 'wire'),       # Put the wire into Box 0
    (None, 5, 'dress'),      # Put the dress into Box 5
    (5, 6, 'bag'),           # Move the bag from Box 5 to Box 6
    (5, 6, 'dress'),         # Move the dress from Box 5 to Box 6
    (6, 2, 'bag'),           # Move the bag from Box 6 to Box 2
    (6, 2, 'computer'),      # Move the computer from Box 6 to Box 2
    (6, 2, 'dress')          # Move the dress from Box 6 to Box 2
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