# Initialize the boxes
boxes = {
    0: ['wheel'],
    1: ['disk', 'guitar', 'letter'],
    2: ['bread', 'fan', 'map'],
    3: ['branch', 'picture'],
    4: ['apple', 'bell', 'boat'],
    5: ['coat', 'jacket', 'tea'],
    6: ['hat'],
}

# Define the moves
moves = [
    (3, 6, 'branch'),       # Move the branch from Box 3 to Box 6
    (3, 6, 'picture'),      # Move the picture from Box 3 to Box 6
    (2, None, 'bread'),     # Remove the bread from Box 2
    (2, None, 'fan'),       # Remove the fan from Box 2
    (2, None, 'map'),       # Remove the map from Box 2
    (6, 2, 'branch'),       # Move the branch from Box 6 to Box 2
    (None, 0, 'pipe'),      # Put the pipe into Box 0
    (4, None, 'apple'),     # Remove the apple from Box 4
    (4, None, 'boat'),      # Remove the boat from Box 4
    (4, None, 'bell'),      # Remove the bell from Box 4
    (5, None, 'coat'),      # Remove the coat from Box 5
    (6, None, 'picture'),   # Remove the picture from Box 6
    (2, None, 'branch'),    # Remove the branch from Box 2
    (0, None, 'pipe'),      # Remove the pipe from Box 0
    (0, None, 'wheel'),     # Remove the wheel from Box 0
    (1, 0, 'guitar'),       # Move the guitar from Box 1 to Box 0
    (5, 6, 'tea')           # Move the tea from Box 5 to Box 6
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