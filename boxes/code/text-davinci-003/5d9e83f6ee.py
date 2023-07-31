# Initialize the boxes
boxes = {
    0: ['apple', 'fig', 'seed'],
    1: ['cigarette', 'ice', 'plant'],
    2: ['bell', 'cake', 'coffee'],
    3: ['tissue'],
    4: [],
    5: [],
    6: ['map'],
}

# Define the moves
moves = [
    (3, 4, 'tissue'),       # Move the tissue from Box 3 to Box 4
    (1, None, 'cigarette'),  # Remove the cigarette from Box 1
    (2, None, 'bell'),       # Remove the bell from Box 2
    (2, None, 'cake'),       # Remove the cake from Box 2
    (None, 5, 'flower'),     # Put the flower into Box 5
    (None, 5, 'pot'),        # Put the pot into Box 5
    (None, 6, 'crown'),      # Put the crown into Box 6
    (2, None, 'coffee'),     # Remove the coffee from Box 2
    (1, 2, 'plant'),         # Move the plant from Box 1 to Box 2
    (0, 4, 'fig'),           # Move the fig from Box 0 to Box 4
    (None, 2, 'radio'),      # Put the radio into Box 2
    (4, None, 'tissue'),     # Remove the tissue from Box 4
    (4, None, 'fig')         # Remove the fig from Box 4
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