# Initialize the boxes
boxes = {
    0: ['bag', 'beer', 'file'],
    1: [],
    2: ['camera', 'radio'],
    3: [],
    4: ['plane', 'shirt', 'wire'],
    5: ['string'],
    6: ['bottle', 'tea'],
}

# Define the moves
moves = [
    (5, 6, 'string'),       # Move the string from Box 5 to Box 6
    (4, 3, 'plane'),        # Move the plane from Box 4 to Box 3
    (3, 5, 'plane'),        # Move the plane from Box 3 to Box 5
    (5, None, 'plane'),     # Remove the plane from Box 5
    (4, None, 'shirt'),     # Remove the shirt from Box 4
    (0, 5, 'beer'),         # Move the beer from Box 0 to Box 5
    (6, None, 'string'),    # Remove the string from Box 6
    (2, None, 'camera'),    # Remove the camera from Box 2
    (None, 4, 'picture'),   # Put the picture into Box 4
    (6, 5, 'tea'),          # Move the tea from Box 6 to Box 5
    (None, 6, 'gift'),      # Put the gift into Box 6
    (2, None, 'radio')      # Remove the radio from Box 2
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