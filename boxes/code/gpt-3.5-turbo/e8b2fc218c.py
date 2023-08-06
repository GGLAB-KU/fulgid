# Initialize the boxes
boxes = {
    0: [],
    1: ['clock', 'map', 'rose'],
    2: ['bread', 'coffee', 'drink'],
    3: [],
    4: [],
    5: ['ring'],
    6: ['jacket', 'key', 'shirt'],
}

# Define the moves
moves = [
    (None, 5, 'fig'),       # Put the fig into Box 5
    (6, None, 'jacket'),    # Remove the jacket from Box 6
    (6, None, 'key'),       # Remove the key from Box 6
    (None, 3, 'car'),       # Put the car into Box 3
    (None, 3, 'dish'),      # Put the dish into Box 3
    (None, 5, 'flower'),    # Put the flower into Box 5
    (2, None, 'coffee'),    # Remove the coffee from Box 2
    (2, None, 'drink'),     # Remove the drink from Box 2
    (1, 4, 'clock'),        # Move the clock from Box 1 to Box 4
    (1, 4, 'rose'),         # Move the rose from Box 1 to Box 4
    (2, 6, 'bread'),        # Move the bread from Box 2 to Box 6
    (None, 6, 'shoe'),      # Put the shoe into Box 6
    (1, None, 'map'),       # Remove the map from Box 1
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