# Initialize the boxes
boxes = {
    0: ['bell', 'phone'],
    1: ['note', 'rock'],
    2: ['dish', 'egg', 'rose'],
    3: ['ice', 'tissue'],
    4: ['ring'],
    5: ['boat', 'meat', 'pot'],
    6: ['map'],
}

# Define the moves
moves = [
    (1, 3, 'note'),         # Move the note from Box 1 to Box 3
    (4, None, 'ring'),      # Remove the ring from Box 4
    (None, 6, 'suit'),      # Put the suit into Box 6
    (3, None, 'ice'),       # Remove the ice from Box 3
    (3, None, 'note'),      # Remove the note from Box 3
    (3, None, 'tissue'),    # Remove the tissue from Box 3
    (1, None, 'rock'),      # Remove the rock from Box 1
    (None, 3, 'apple'),     # Put the apple into Box 3
    (5, None, 'meat'),      # Remove the meat from Box 5
    (3, 6, 'apple'),        # Move the apple from Box 3 to Box 6
    (2, 3, 'rose'),         # Move the rose from Box 2 to Box 3
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