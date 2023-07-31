# Initialize the boxes
boxes = {
    0: ['clock', 'game'],
    1: ['fig'],
    2: ['mirror'],
    3: ['bill', 'creature', 'phone'],
    4: ['ice', 'rock'],
    5: ['pipe'],
    6: ['brick', 'leaf'],
}

# Define the moves
moves = [
    (2, 1, 'mirror'),       # Move the mirror from Box 2 to Box 1
    (None, 1, 'apple'),     # Put the apple into Box 1
    (None, 5, 'jacket'),    # Put the jacket into Box 5
    (4, None, 'ice'),       # Remove the ice from Box 4
    (4, None, 'rock'),      # Remove the rock from Box 4
    (6, 2, 'brick'),        # Move the brick from Box 6 to Box 2
    (1, 6, 'apple'),        # Move the apple from Box 1 to Box 6
    (5, 2, 'jacket'),       # Move the jacket from Box 5 to Box 2
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