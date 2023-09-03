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
    (0, None, 'picture'),    # Remove the picture from Box 0
    (0, None, 'seed'),       # Remove the seed from Box 0
    (0, None, 'watch'),      # Remove the watch from Box 0
    (None, 3, 'apple'),      # Put the apple into Box 3
    (None, 3, 'branch'),     # Put the branch into Box 3
    (None, 3, 'bread'),      # Put the bread into Box 3
    (4, None, 'milk'),       # Remove the milk from Box 4
    (4, None, 'wheel'),      # Remove the wheel from Box 4
    (None, 5, 'ball'),       # Put the ball into Box 5
    (None, 5, 'chemical'),   # Put the chemical into Box 5
    (6, None, 'brick'),      # Remove the brick from Box 6
    (6, None, 'tea'),        # Remove the tea from Box 6
    (6, None, 'wire'),       # Remove the wire from Box 6
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