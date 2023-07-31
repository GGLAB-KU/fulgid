# Initialize the boxes
boxes = {
    0: ['cigarette', 'dress', 'string'],
    1: ['disk', 'stone'],
    2: [],
    3: [],
    4: ['bread', 'fig', 'tape'],
    5: [],
    6: ['watch'],
}

# Define the moves
moves = [
    (4, 2, 'tape'),         # Move the tape from Box 4 to Box 2
    (4, 3, 'bread'),        # Move the bread from Box 4 to Box 3
    (4, 3, 'fig'),          # Move the fig from Box 4 to Box 3
    (3, None, 'bread'),     # Remove the bread from Box 3
    (3, None, 'fig'),       # Remove the fig from Box 3
    (2, None, 'tape'),      # Remove the tape from Box 2
    (6, None, 'watch'),     # Remove the watch from Box 6
    (0, 3, 'cigarette'),    # Move the cigarette from Box 0 to Box 3
    (0, 3, 'dress'),        # Move the dress from Box 0 to Box 3
    (0, 3, 'string'),       # Move the string from Box 0 to Box 3
    (None, 5, 'cup'),       # Put the cup into Box 5
    (None, 5, 'engine'),    # Put the engine into Box 5
    (3, None, 'string'),    # Remove the string from Box 3
    (5, 2, 'cup'),          # Move the cup from Box 5 to Box 2
    (3, None, 'dress'),     # Remove the dress from Box 3
    (2, 0, 'cup')           # Move the cup from Box 2 to Box 0
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