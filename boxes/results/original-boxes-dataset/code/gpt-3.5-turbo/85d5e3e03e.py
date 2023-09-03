# Initialize the boxes
boxes = {
    0: ['boot', 'key', 'pipe'],
    1: ['branch', 'drug', 'meat'],
    2: ['fig', 'radio', 'tissue'],
    3: ['machine', 'painting', 'watch'],
    4: ['crown', 'plate', 'pot'],
    5: ['bag', 'cross', 'disk'],
    6: ['leaf', 'letter', 'shell'],
}

# Define the moves
moves = [
    (3, None, 'watch'),     # Remove the watch from Box 3
    (4, None, 'pot'),       # Remove the pot from Box 4
    (1, None, 'meat'),      # Remove the meat from Box 1
    (None, 4, 'bell'),      # Put the bell into Box 4
    (None, 3, 'sheet'),     # Put the sheet into Box 3
    (1, None, 'drug'),      # Remove the drug from Box 1
    (0, None, 'boot'),      # Remove the boot from Box 0
    (0, None, 'pipe'),      # Remove the pipe from Box 0
    (2, 1, 'fig'),          # Move the fig from Box 2 to Box 1
    (4, None, 'crown'),     # Remove the crown from Box 4
    (4, None, 'plate'),     # Remove the plate from Box 4
    (2, None, 'radio'),     # Remove the radio from Box 2
    (6, 2, 'leaf'),         # Move the leaf from Box 6 to Box 2
    (2, 4, 'leaf'),         # Move the leaf from Box 2 to Box 4
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