# Initialize the boxes
boxes = {
    0: [],
    1: ['file', 'plane'],
    2: ['crown'],
    3: ['picture', 'shirt'],
    4: ['plate', 'radio'],
    5: [],
    6: ['television', 'ticket'],
}

# Define the moves
moves = [
    (3, 2, 'shirt'),        # Move the shirt from Box 3 to Box 2
    (2, None, 'crown'),     # Remove the crown from Box 2
    (2, None, 'shirt'),     # Remove the shirt from Box 2
    (6, None, 'ticket'),    # Remove the ticket from Box 6
    (3, 6, 'picture'),      # Move the picture from Box 3 to Box 6
    (None, 5, 'apple'),     # Put the apple into Box 5
    (None, 5, 'coffee'),    # Put the coffee into Box 5
    (None, 5, 'wire'),      # Put the wire into Box 5
    (1, 6, 'file'),         # Move the file from Box 1 to Box 6
    (6, None, 'picture'),   # Remove the picture from Box 6
    (6, None, 'television'), # Remove the television from Box 6
    (6, None, 'file'),      # Remove the file from Box 6
    (1, 6, 'plane'),        # Move the plane from Box 1 to Box 6
    (6, 2, 'plane'),        # Move the plane from Box 6 to Box 2
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