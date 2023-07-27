# Initialize the boxes
boxes = {
    0: [],
    1: ['egg', 'letter'],
    2: ['knife', 'shell', 'train'],
    3: ['brick', 'jacket', 'mirror'],
    4: ['document', 'radio'],
    5: ['disk'],
    6: ['bottle', 'coat', 'computer'],
}

# Define the moves
moves = [
    (2, None, 'knife'),     # Remove the knife from Box 2
    (2, None, 'shell'),     # Remove the shell from Box 2
    (2, None, 'train'),     # Remove the train from Box 2
    (1, None, 'egg'),       # Remove the egg from Box 1
    (None, 2, 'newspaper'),  # Put the newspaper into Box 2
    (None, 0, 'pipe'),      # Put the pipe into Box 0
    (None, 0, 'ring'),      # Put the ring into Box 0
    (6, 0, 'computer'),     # Move the computer from Box 6 to Box 0
    (6, None, 'coat'),      # Remove the coat from Box 6
    (3, 1, 'brick'),        # Move the brick from Box 3 to Box 1
    (3, 1, 'mirror'),       # Move the mirror from Box 3 to Box 1
    (0, None, 'pipe'),      # Remove the pipe from Box 0
    (2, None, 'egg'),       # Put the egg into Box 2
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