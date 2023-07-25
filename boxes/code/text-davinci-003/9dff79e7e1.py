# Initialize the boxes
boxes = {
    0: ['apple'],
    1: ['block', 'document', 'jacket'],
    2: ['machine'],
    3: [],
    4: ['sheet', 'tissue'],
    5: ['egg', 'ice'],
    6: ['mirror', 'plane', 'string'],
}

# Define the moves
moves = [
    (5, None, 'ice'),       # Remove the ice from Box 5
    (0, None, 'apple'),     # Remove the apple from Box 0
    (5, None, 'egg'),       # Remove the egg from Box 5
    (4, None, 'sheet'),     # Remove the sheet from Box 4
    (None, 4, 'cash'),      # Put the cash into Box 4
    (None, 4, 'glass'),     # Put the glass into Box 4
    (4, None, 'cash'),      # Remove the cash from Box 4
    (4, None, 'glass'),     # Remove the glass from Box 4
    (None, 4, 'sheet'),     # Put the sheet into Box 4
    (None, 2, 'bag'),       # Put the bag into Box 2
    (6, None, 'mirror'),    # Remove the mirror from Box 6
    (6, None, 'plane'),     # Remove the plane from Box 6
    (4, 3, 'sheet'),        # Move the sheet from Box 4 to Box 3
    (4, 3, 'tissue'),       # Move the tissue from Box 4 to Box 3
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