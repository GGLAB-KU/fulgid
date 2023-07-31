# Initialize the boxes
boxes = {
    0: ['computer', 'pipe', 'wire'],
    1: ['bottle', 'stone', 'tape'],
    2: ['crown', 'letter'],
    3: ['car', 'magazine', 'note'],
    4: ['bus', 'flower', 'tie'],
    5: ['cheese', 'drink', 'sheet'],
    6: ['camera', 'leaf', 'rock'],
}

# Define the moves
moves = [
    (4, None, 'bus'),       # Remove the bus from Box 4
    (6, None, 'leaf'),      # Remove the leaf from Box 6
    (6, None, 'rock'),      # Remove the rock from Box 6
    (3, None, 'car'),       # Remove the car from Box 3
    (3, None, 'magazine'),  # Remove the magazine from Box 3
    (None, 3, 'shell'),     # Put the shell into Box 3
    (2, 4, 'crown'),        # Move the crown from Box 2 to Box 4
    (1, 2, 'bottle'),       # Move the bottle from Box 1 to Box 2
    (5, 3, 'cheese'),       # Move the cheese from Box 5 to Box 3
    (3, None, 'note'),      # Remove the note from Box 3
    (3, None, 'shell'),     # Remove the shell from Box 3
    (6, None, 'camera'),    # Remove the camera from Box 6
    (None, 3, 'egg')        # Put the egg into Box 3
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