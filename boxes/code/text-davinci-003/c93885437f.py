# Initialize the boxes
boxes = {
    0: ['boat', 'leaf'],
    1: ['cash'],
    2: [],
    3: ['key', 'map', 'picture'],
    4: ['ring'],
    5: ['coffee'],
    6: ['chemical', 'guitar'],
}

# Define the moves
moves = [
    (None, 6, 'fish'),       # Put the fish into Box 6
    (4, None, 'ring'),       # Remove the ring from Box 4
    (None, 4, 'bottle'),     # Put the bottle into Box 4
    (6, 0, 'fish'),          # Move the fish from Box 6 to Box 0
    (None, 5, 'pot'),        # Put the pot into Box 5
    (6, None, 'guitar'),     # Remove the guitar from Box 6
    (6, 5, 'chemical'),      # Move the chemical from Box 6 to Box 5
    (5, None, 'coffee'),     # Remove the coffee from Box 5
    (5, None, 'chemical'),   # Remove the chemical from Box 5
    (5, None, 'pot'),        # Remove the pot from Box 5
    (3, 5, 'map'),           # Move the map from Box 3 to Box 5
    (3, 5, 'picture')        # Move the picture from Box 3 to Box 5
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