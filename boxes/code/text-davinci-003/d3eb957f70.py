# Initialize the boxes
boxes = {
    0: ['bill', 'mirror', 'shoe'],
    1: ['clock', 'dress', 'fig'],
    2: ['computer', 'knife', 'tie'],
    3: ['rock'],
    4: ['creature', 'file'],
    5: ['stone'],
    6: ['beer', 'seed'],
}

# Define the moves
moves = [
    (5, 3, 'stone'),        # Move the stone from Box 5 to Box 3
    (None, 3, 'cheese'),    # Put the cheese into Box 3
    (3, None, 'cheese'),    # Remove the cheese from Box 3
    (3, None, 'rock'),      # Remove the rock from Box 3
    (3, None, 'stone'),     # Remove the stone from Box 3
    (4, None, 'creature'),  # Remove the creature from Box 4
    (0, 3, 'bill'),         # Move the bill from Box 0 to Box 3
    (0, 3, 'mirror'),       # Move the mirror from Box 0 to Box 3
    (0, 3, 'shoe'),         # Move the shoe from Box 0 to Box 3
    (None, 6, 'shirt'),     # Put the shirt into Box 6
    (3, None, 'bill'),      # Remove the bill from Box 3
    (3, None, 'mirror'),    # Remove the mirror from Box 3
    (6, None, 'seed'),      # Remove the seed from Box 6
    (6, None, 'shirt'),     # Remove the shirt from Box 6
    (1, 4, 'clock'),        # Move the clock from Box 1 to Box 4
    (1, 4, 'dress'),        # Move the dress from Box 1 to Box 4
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