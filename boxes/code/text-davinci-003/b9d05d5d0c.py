# Initialize the boxes
boxes = {
    0: ['map'],
    1: [],
    2: [],
    3: ['bus', 'plane'],
    4: ['brick', 'drink', 'pipe'],
    5: ['ice'],
    6: ['cake', 'chemical', 'rose'],
}

# Define the moves
moves = [
    (5, None, 'ice'),       # Remove the ice from Box 5
    (None, 3, 'document'),  # Put the document into Box 3
    (None, 1, 'engine'),    # Put the engine into Box 1
    (None, 1, 'hat'),       # Put the hat into Box 1
    (1, 2, 'engine'),       # Move the engine from Box 1 to Box 2
    (6, None, 'cake'),      # Remove the cake from Box 6
    (6, None, 'chemical'),  # Remove the chemical from Box 6
    (4, None, 'brick'),     # Remove the brick from Box 4
    (4, None, 'drink'),     # Remove the drink from Box 4
    (0, 4, 'map'),          # Move the map from Box 0 to Box 4
    (None, 6, 'block'),     # Put the block into Box 6
    (None, 6, 'leaf'),      # Put the leaf into Box 6
    (None, 4, 'bell'),      # Put the bell into Box 4
    (4, None, 'map'),       # Remove the map from Box 4
    (1, None, 'hat'),       # Remove the hat from Box 1
    (6, None, 'block'),     # Remove the block from Box 6
    (6, None, 'leaf')       # Remove the leaf from Box 6
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