# Initialize the boxes
boxes = {
    0: ['bill', 'cash', 'disk'],
    1: ['file'],
    2: ['egg', 'radio', 'shell'],
    3: ['book', 'bottle', 'cake'],
    4: ['ticket'],
    5: ['brain', 'plate'],
    6: ['plant'],
}

# Define the moves
moves = [
    (2, None, 'egg'),       # Remove the egg from Box 2
    (2, None, 'shell'),     # Remove the shell from Box 2
    (5, 1, 'brain'),        # Move the brain from Box 5 to Box 1
    (0, None, 'bill'),      # Remove the bill from Box 0
    (0, None, 'cash'),      # Remove the cash from Box 0
    (0, None, 'disk'),      # Remove the disk from Box 0
    (6, 4, 'plant'),        # Move the plant from Box 6 to Box 4
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