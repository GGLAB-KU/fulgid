# Initialize the boxes
boxes = {
    0: ['mirror', 'shirt', 'string'],
    1: [],
    2: ['camera', 'drink'],
    3: ['bottle', 'shoe', 'television'],
    4: ['cash', 'newspaper'],
    5: ['phone', 'tissue'],
    6: ['boat', 'cheese', 'letter'],
}

# Define the moves
moves = [
    (6, None, 'boat'),       # Remove the boat from Box 6
    (6, None, 'cheese'),     # Remove the cheese from Box 6
    (None, 2, 'fish'),       # Put the fish into Box 2
    (4, None, 'cash'),       # Remove the cash from Box 4
    (4, None, 'newspaper'),  # Remove the newspaper from Box 4
    (5, None, 'phone'),      # Remove the phone from Box 5
    (2, 4, 'drink'),         # Move the drink from Box 2 to Box 4
    (2, 4, 'fish'),          # Move the fish from Box 2 to Box 4
    (None, 5, 'bowl'),       # Put the bowl into Box 5
    (None, 5, 'tea'),        # Put the tea into Box 5
    (2, 4, 'camera'),        # Move the camera from Box 2 to Box 4
    (3, None, 'television'),  # Remove the television from Box 3
    (0, None, 'mirror'),     # Remove the mirror from Box 0
    (0, None, 'shirt'),      # Remove the shirt from Box 0
    (4, None, 'camera'),     # Remove the camera from Box 4
    (4, None, 'drink')       # Remove the drink from Box 4
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