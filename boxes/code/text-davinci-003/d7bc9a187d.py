# Initialize the boxes
boxes = {
    0: ['shoe', 'wheel'],
    1: ['beer', 'file', 'pot'],
    2: ['creature', 'engine', 'ring'],
    3: [],
    4: ['magazine'],
    5: [],
    6: [],
}

# Define the moves
moves = [
    (0, None, 'wheel'),       # Remove the wheel from Box 0
    (2, 3, 'engine'),         # Move the engine from Box 2 to Box 3
    (2, 3, 'ring'),           # Move the ring from Box 2 to Box 3
    (0, 3, 'shoe'),           # Move the shoe from Box 0 to Box 3
    (2, None, 'creature'),    # Remove the creature from Box 2
    (None, 5, 'meat'),        # Put the meat into Box 5
    (4, None, 'magazine'),    # Remove the magazine from Box 4
    (5, None, 'meat')         # Remove the meat from Box 5
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