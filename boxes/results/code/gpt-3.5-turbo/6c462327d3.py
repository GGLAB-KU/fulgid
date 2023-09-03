# Initialize the boxes
boxes = {
    0: ['beer', 'cup', 'phone'],
    1: ['boat', 'seed', 'shirt'],
    2: ['wire'],
    3: ['mirror', 'suit'],
    4: ['bread', 'key', 'plane'],
    5: ['car', 'ticket'],
    6: ['drink'],
}

# Define the moves
moves = [
    (1, None, 'boat'),      # Remove the boat from Box 1
    (1, None, 'shirt'),     # Remove the shirt from Box 1
    (None, 1, 'file'),      # Put the file into Box 1
    (1, None, 'file'),      # Remove the file from Box 1
    (1, None, 'seed'),      # Remove the seed from Box 1
    (6, None, 'drink'),     # Remove the drink from Box 6
    (3, None, 'mirror'),    # Remove the mirror from Box 3
    (2, None, 'wire'),      # Remove the wire from Box 2
    (0, None, 'cup'),       # Remove the cup from Box 0
    (0, None, 'phone'),     # Remove the phone from Box 0
    (None, 5, 'picture'),   # Put the picture into Box 5
    (4, None, 'key'),       # Remove the key from Box 4
    (4, None, 'plane'),     # Remove the plane from Box 4
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