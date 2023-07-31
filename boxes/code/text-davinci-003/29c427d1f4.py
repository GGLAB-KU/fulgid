# Initialize the boxes
boxes = {
    0: [],
    1: ['bag', 'cream'],
    2: ['plant', 'sheet', 'tape'],
    3: ['block', 'plane'],
    4: ['boat', 'clock', 'crown'],
    5: ['paper'],
    6: [],
}

# Define the moves
moves = [
    (4, None, 'boat'),       # Remove the boat from Box 4
    (4, 0, 'crown'),         # Move the crown from Box 4 to Box 0
    (None, 4, 'ticket'),     # Put the ticket into Box 4
    (5, 0, 'paper'),         # Move the paper from Box 5 to Box 0
    (None, 6, 'cheese'),     # Put the cheese into Box 6
    (None, 6, 'egg'),        # Put the egg into Box 6
    (4, None, 'clock'),      # Remove the clock from Box 4
    (4, None, 'ticket'),     # Remove the ticket from Box 4
    (None, 0, 'meat'),       # Put the meat into Box 0
    (None, 5, 'disk'),       # Put the disk into Box 5
    (3, 6, 'plane'),         # Move the plane from Box 3 to Box 6
    (3, None, 'block'),      # Remove the block from Box 3
    (None, 4, 'shell'),      # Put the shell into Box 4
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