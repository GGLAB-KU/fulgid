# Initialize the boxes
boxes = {
    0: ['leaf'],
    1: [],
    2: ['block', 'camera', 'knife'],
    3: ['crown', 'mirror', 'tissue'],
    4: ['gift', 'pipe'],
    5: ['ice'],
    6: ['brick', 'picture', 'watch'],
}

# Define the moves
moves = [
    (0, None, 'leaf'),       # Remove the leaf from Box 0
    (3, 1, 'mirror'),        # Move the mirror from Box 3 to Box 1
    (6, None, 'brick'),      # Remove the brick from Box 6
    (6, None, 'watch'),      # Remove the watch from Box 6
    (6, None, 'picture'),    # Remove the picture from Box 6
    (None, 6, 'card'),       # Put the card into Box 6
    (None, 6, 'document'),   # Put the document into Box 6
    (None, 6, 'letter'),     # Put the letter into Box 6
    (1, None, 'mirror'),     # Remove the mirror from Box 1
    (None, 1, 'cross'),      # Put the cross into Box 1
    (4, 1, 'gift'),          # Move the gift from Box 4 to Box 1
    (4, 1, 'pipe')           # Move the pipe from Box 4 to Box 1
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