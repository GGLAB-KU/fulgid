# Initialize the boxes
boxes = {
    0: ['chemical', 'cup'],
    1: ['book', 'game', 'magazine'],
    2: ['boat', 'fig', 'hat'],
    3: ['car', 'seed', 'suit'],
    4: ['drug', 'leaf', 'painting'],
    5: [],
    6: [],
}

# Define the moves
moves = [
    (1, None, 'book'),       # Remove the book from Box 1
    (1, None, 'magazine'),   # Remove the magazine from Box 1
    (0, None, 'chemical'),   # Remove the chemical from Box 0
    (None, 6, 'bread'),      # Put the bread into Box 6
    (None, 6, 'mirror'),     # Put the mirror into Box 6
    (6, 1, 'mirror'),        # Move the mirror from Box 6 to Box 1
    (1, None, 'game'),       # Remove the game from Box 1
    (None, 1, 'plane'),      # Put the plane into Box 1
    (2, None, 'fig'),        # Remove the fig from Box 2
    (2, None, 'hat'),        # Remove the hat from Box 2
    (6, None, 'bread'),      # Remove the bread from Box 6
    (None, 5, 'bus'),        # Put the bus into Box 5
    (None, 5, 'cheese'),     # Put the cheese into Box 5
    (0, 1, 'cup'),           # Move the cup from Box 0 to Box 1
    (1, None, 'cup')         # Remove the cup from Box 1
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