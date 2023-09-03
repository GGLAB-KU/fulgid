# Initialize the boxes
boxes = {
    0: ['cash', 'wheel', 'wire'],
    1: ['cake', 'drink', 'fish'],
    2: ['ticket'],
    3: [],
    4: ['brain', 'bread', 'ring'],
    5: ['radio', 'string'],
    6: ['branch', 'coat'],
}

# Define the moves
moves = [
    (0, None, 'cash'),      # Remove the cash from Box 0
    (0, None, 'wheel'),     # Remove the wheel from Box 0
    (0, None, 'wire'),      # Remove the wire from Box 0
    (None, 0, 'fig'),       # Put the fig into Box 0
    (None, 0, 'plate'),     # Put the plate into Box 0
    (None, 0, 'suit'),      # Put the suit into Box 0
    (None, 3, 'coffee'),    # Put the coffee into Box 3
    (4, None, 'bread'),     # Remove the bread from Box 4
    (4, None, 'ring'),      # Remove the ring from Box 4
    (6, 2, 'branch'),       # Move the branch from Box 6 to Box 2
    (6, 2, 'coat'),         # Move the coat from Box 6 to Box 2
    (None, 3, 'letter')     # Put the letter into Box 3
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