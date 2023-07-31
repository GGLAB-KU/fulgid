# Initialize the boxes
boxes = {
    0: ['knife'],
    1: [],
    2: ['ball', 'rose'],
    3: ['suit'],
    4: ['key', 'plate', 'ring'],
    5: ['fan', 'meat'],
    6: ['file', 'sheet'],
}

# Define the moves
moves = [
    (3, 2, 'suit'),         # Move the suit from Box 3 to Box 2
    (2, 3, 'suit'),         # Move the suit from Box 2 to Box 3
    (6, 2, 'sheet'),        # Move the sheet from Box 6 to Box 2
    (5, None, 'fan'),       # Remove the fan from Box 5
    (5, None, 'meat'),      # Remove the meat from Box 5
    (3, None, 'suit'),      # Remove the suit from Box 3
    (6, 5, 'file'),         # Move the file from Box 6 to Box 5
    (0, None, 'knife'),     # Remove the knife from Box 0
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