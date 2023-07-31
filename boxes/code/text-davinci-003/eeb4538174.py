# Initialize the boxes
boxes = {
    0: ['picture', 'seed', 'watch'],
    1: ['crown'],
    2: ['bus', 'pot', 'suit'],
    3: ['apple', 'branch', 'bread'],
    4: ['milk', 'wheel'],
    5: ['ball', 'chemical'],
    6: ['brick', 'tea', 'wire'],
}

# Define the moves
moves = [
    (2, None, 'bus'),       # Remove the bus from Box 2
    (2, None, 'pot'),       # Remove the pot from Box 2
    (6, None, 'brick'),     # Remove the brick from Box 6
    (6, None, 'tea'),       # Remove the tea from Box 6
    (6, None, 'wire'),      # Remove the wire from Box 6
    (1, None, 'crown'),     # Remove the crown from Box 1
    (3, None, 'branch'),    # Remove the branch from Box 3
    (None, 6, 'note'),      # Put the note into Box 6
    (2, 3, 'suit'),         # Move the suit from Box 2 to Box 3
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