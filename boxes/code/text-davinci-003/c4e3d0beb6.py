# Initialize the boxes
boxes = {
    0: ['pipe'],
    1: [],
    2: ['plane'],
    3: ['bomb'],
    4: ['machine', 'ring', 'rose'],
    5: ['plate'],
    6: ['picture'],
}

# Define the moves
moves = [
    (5, None, 'plate'),     # Remove the plate from Box 5
    (2, None, 'plane'),     # Remove the plane from Box 2
    (4, 0, 'machine'),      # Move the machine from Box 4 to Box 0
    (6, None, 'picture'),   # Remove the picture from Box 6
    (0, None, 'pipe'),      # Remove the pipe from Box 0
    (None, 4, 'letter'),    # Put the letter into Box 4
    (4, 6, 'letter'),       # Move the letter from Box 4 to Box 6
    (4, 6, 'ring'),         # Move the ring from Box 4 to Box 6
    (6, 3, 'letter'),       # Move the letter from Box 6 to Box 3
    (3, None, 'bomb'),      # Remove the bomb from Box 3
    (None, 3, 'beer'),      # Put the beer into Box 3
    (None, 3, 'ticket'),    # Put the ticket into Box 3
    (6, 2, 'ring'),         # Move the ring from Box 6 to Box 2
    (4, 5, 'rose'),         # Move the rose from Box 4 to Box 5
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