# Initialize the boxes
boxes = {
    0: ['cup', 'dress'],
    1: ['engine', 'jacket', 'paper'],
    2: [],
    3: [],
    4: ['bone', 'fish'],
    5: ['plate'],
    6: ['note'],
}

# Define the moves
moves = [
    (1, None, 'engine'),    # Remove the engine from Box 1
    (1, None, 'jacket'),    # Remove the jacket from Box 1
    (1, None, 'paper'),     # Remove the paper from Box 1
    (6, None, 'note'),      # Remove the note from Box 6
    (0, 1, 'cup'),          # Move the cup from Box 0 to Box 1
    (5, 3, 'plate'),        # Move the plate from Box 5 to Box 3
    (4, 2, 'bone'),         # Move the bone from Box 4 to Box 2
    (4, 2, 'fish'),         # Move the fish from Box 4 to Box 2
    (3, None, 'plate'),     # Remove the plate from Box 3
    (1, None, 'cup'),       # Remove the cup from Box 1
    (2, None, 'bone'),      # Remove the bone from Box 2
    (None, 3, 'shell'),     # Put the shell into Box 3
    (3, None, 'shell')      # Remove the shell from Box 3
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