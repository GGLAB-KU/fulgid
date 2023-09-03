# Initialize the boxes
boxes = {
    0: ['bowl', 'bread', 'suit'],
    1: ['medicine'],
    2: ['ball', 'egg'],
    3: [],
    4: ['fish'],
    5: ['glass', 'tie'],
    6: [],
}

# Define the moves
moves = [
    (1, 4, 'medicine'),     # Move the medicine from Box 1 to Box 4
    (0, None, 'bowl'),      # Remove the bowl from Box 0
    (5, None, 'glass'),     # Remove the glass from Box 5
    (5, None, 'tie'),       # Remove the tie from Box 5
    (0, None, 'bread'),     # Remove the bread from Box 0
    (2, 0, 'ball'),         # Move the ball from Box 2 to Box 0
    (4, None, 'fish'),      # Remove the fish from Box 4
    (1, 2, 'medicine'),     # Remove the medicine from Box 1 and put it into Box 2
    (None, 2, 'cheese'),    # Put the cheese into Box 2
    (None, 2, 'fan'),       # Put the fan into Box 2
    (2, None, 'egg'),       # Remove the egg from Box 2
    (None, 0, 'chemical'),  # Put the chemical into Box 0
    (0, 6, 'chemical'),     # Move the chemical from Box 0 to Box 6
    (0, 6, 'suit')          # Move the suit from Box 0 to Box 6
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