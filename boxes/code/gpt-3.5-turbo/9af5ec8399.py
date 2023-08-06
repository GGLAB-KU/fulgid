# Initialize the boxes
boxes = {
    0: ['ball'],
    1: ['radio'],
    2: ['clock', 'map', 'note'],
    3: ['coat'],
    4: ['bottle', 'bus', 'pipe'],
    5: ['bag', 'phone', 'tissue'],
    6: ['computer', 'meat', 'shoe'],
}

# Define the moves
moves = [
    (3, 1, 'coat'),         # Move the coat from Box 3 to Box 1
    (1, None, 'coat'),      # Remove the coat from Box 1
    (1, None, 'radio'),     # Remove the radio from Box 1
    (4, None, 'bus'),       # Remove the bus from Box 4
    (4, None, 'pipe'),      # Remove the pipe from Box 4
    (2, 0, 'map'),          # Move the map from Box 2 to Box 0
    (2, 0, 'note'),         # Move the note from Box 2 to Box 0
    (0, 1, 'map'),          # Move the map from Box 0 to Box 1
    (0, None, 'note'),      # Remove the note from Box 0
    (1, 2, 'map'),          # Move the map from Box 1 to Box 2
    (5, None, 'bag'),       # Remove the bag from Box 5
    (5, None, 'phone'),     # Remove the phone from Box 5
    (5, None, 'tissue'),    # Remove the tissue from Box 5
    (None, 0, 'apple'),     # Put the apple into Box 0
    (None, 0, 'flower'),    # Put the flower into Box 0
    (0, None, 'ball'),      # Remove the ball from Box 0
    (0, None, 'flower'),    # Remove the flower from Box 0
    (6, 3, 'meat'),         # Move the meat from Box 6 to Box 3
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