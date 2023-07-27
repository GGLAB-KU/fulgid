# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: [],
    3: ['clock', 'file', 'plant'],
    4: ['sheet', 'television', 'wheel'],
    5: ['brick', 'coat', 'radio'],
    6: ['block', 'branch', 'disk'],
}

# Define the moves
moves = [
    (3, 1, 'file'),         # Move the file from Box 3 to Box 1
    (3, 1, 'plant'),        # Move the plant from Box 3 to Box 1
    (None, 3, 'train'),     # Put the train into Box 3
    (5, 0, 'coat'),         # Move the coat from Box 5 to Box 0
    (5, 0, 'radio'),        # Move the radio from Box 5 to Box 0
    (5, 3, 'brick'),        # Move the brick from Box 5 to Box 3
    (0, None, 'radio'),     # Remove the radio from Box 0
    (0, None, 'boot'),      # Put the boot into Box 0
    (4, None, 'sheet'),     # Remove the sheet from Box 4
    (0, 2, 'boot'),         # Move the boot from Box 0 to Box 2
    (2, 1, 'boot'),         # Move the boot from Box 2 to Box 1
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