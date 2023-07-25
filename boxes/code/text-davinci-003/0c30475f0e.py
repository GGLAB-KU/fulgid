# Initialize the boxes
boxes = {
    0: [],
    1: ['bowl', 'disk'],
    2: ['bottle', 'rock', 'wire'],
    3: ['apple', 'ice', 'shirt'],
    4: ['branch', 'card', 'crown'],
    5: ['tie'],
    6: ['leaf', 'ring'],
}

# Define the moves
moves = [
    (5, None, 'tie'),       # Remove the tie from Box 5
    (2, None, 'bottle'),    # Remove the bottle from Box 2
    (2, None, 'rock'),      # Remove the rock from Box 2
    (2, None, 'wire'),      # Remove the wire from Box 2
    (6, None, 'leaf'),      # Remove the leaf from Box 6
    (None, 5, 'machine'),   # Put the machine into Box 5
    (5, None, 'machine'),   # Remove the machine from Box 5
    (1, 5, 'disk'),         # Move the disk from Box 1 to Box 5
    (None, 2, 'flower'),    # Put the flower into Box 2
    (None, 2, 'magazine'),  # Put the magazine into Box 2
    (3, None, 'apple'),     # Remove the apple from Box 3
    (3, None, 'ice'),       # Remove the ice from Box 3
    (1, 6, 'bowl'),         # Move the bowl from Box 1 to Box 6
    (3, 0, 'shirt'),        # Move the shirt from Box 3 to Box 0
    (5, 1, 'disk'),         # Move the disk from Box 5 to Box 1
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