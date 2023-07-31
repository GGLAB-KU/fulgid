# Initialize the boxes
boxes = {
    0: ['cake'],
    1: [],
    2: ['coffee', 'tie'],
    3: ['pipe', 'rock', 'shoe'],
    4: ['bread', 'egg', 'meat'],
    5: [],
    6: ['brick'],
}

# Define the moves
moves = [
    (4, None, 'bread'),     # Remove the bread from Box 4
    (4, None, 'egg'),       # Remove the egg from Box 4
    (None, 4, 'note'),      # Put the note into Box 4
    (None, 1, 'tea'),       # Put the tea into Box 1
    (3, 2, 'shoe'),         # Move the shoe from Box 3 to Box 2
    (3, 5, 'pipe'),         # Move the pipe from Box 3 to Box 5
    (3, 5, 'rock'),         # Move the rock from Box 3 to Box 5
    (6, None, 'brick'),     # Remove the brick from Box 6
    (1, None, 'tea')        # Remove the tea from Box 1
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