# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['block'],
    3: ['sheet'],
    4: ['branch', 'file', 'radio'],
    5: [],
    6: ['computer', 'plant'],
}

# Define the moves
moves = [
    (4, None, 'branch'),    # Remove the branch from Box 4
    (4, None, 'file'),      # Remove the file from Box 4
    (None, 0, 'leaf'),      # Put the leaf into Box 0
    (0, 4, 'leaf'),         # Move the leaf from Box 0 to Box 4
    (6, None, 'computer'),  # Remove the computer from Box 6
    (6, None, 'plant'),     # Remove the plant from Box 6
    (None, 4, 'bag'),       # Put the bag into Box 4
    (None, 0, 'bowl'),      # Put the bowl into Box 0
    (0, None, 'bowl'),      # Remove the bowl from Box 0
    (4, None, 'leaf'),      # Remove the leaf from Box 4
    (3, 2, 'sheet'),        # Move the sheet from Box 3 to Box 2
    (None, 2, 'shirt'),     # Put the shirt into Box 2
    (4, 6, 'bag'),          # Move the bag from Box 4 to Box 6
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