# Initialize the boxes
boxes = {
    0: ['dress', 'string', 'tea'],
    1: [],
    2: ['coat', 'phone'],
    3: ['drug', 'knife'],
    4: [],
    5: ['map', 'pipe', 'tie'],
    6: ['picture'],
}

# Define the moves
moves = [
    (6, None, 'picture'),   # Remove the picture from Box 6
    (3, None, 'drug'),      # Remove the drug from Box 3
    (5, None, 'map'),       # Remove the map from Box 5
    (5, None, 'tie'),       # Remove the tie from Box 5
    (5, 3, 'pipe'),         # Move the pipe from Box 5 to Box 3
    (None, 6, 'bell'),      # Put the bell into Box 6
    (None, 6, 'clock'),     # Put the clock into Box 6
    (2, None, 'phone'),     # Remove the phone from Box 2
    (3, None, 'pipe'),      # Remove the pipe from Box 3
    (3, None, 'knife'),     # Remove the knife from Box 3
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