# Initialize the boxes
boxes = {
    0: ['dress', 'meat', 'tie'],
    1: ['coffee', 'tissue'],
    2: [],
    3: ['fig', 'shirt', 'wheel'],
    4: [],
    5: ['stone'],
    6: ['bomb', 'branch', 'rock'],
}

# Define the moves
moves = [
    (0, None, 'dress'),     # Remove the dress from Box 0
    (0, None, 'meat'),      # Remove the meat from Box 0
    (0, None, 'tie'),       # Remove the tie from Box 0
    (5, 1, 'stone'),        # Move the stone from Box 5 to Box 1
    (1, 0, 'coffee'),       # Move the coffee from Box 1 to Box 0
    (1, 0, 'tissue'),       # Move the tissue from Box 1 to Box 0
    (None, 4, 'engine'),    # Put the engine into Box 4
    (None, 4, 'fan'),       # Put the fan into Box 4
    (None, 4, 'suit'),      # Put the suit into Box 4
    (0, None, 'tissue'),    # Remove the tissue from Box 0
    (4, None, 'engine'),    # Remove the engine from Box 4
    (4, None, 'fan'),       # Remove the fan from Box 4
    (0, 5, 'coffee'),       # Move the coffee from Box 0 to Box 5
    (None, 1, 'cheese'),    # Put the cheese into Box 1
    (1, 4, 'stone'),        # Move the stone from Box 1 to Box 4
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