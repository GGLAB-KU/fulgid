# Initialize the boxes
boxes = {
    0: ['bill', 'bowl', 'meat'],
    1: ['file'],
    2: [],
    3: ['computer', 'ring'],
    4: ['bread', 'crown'],
    5: ['beer', 'bone', 'plate'],
    6: ['egg', 'shirt'],
}

# Define the moves
moves = [
    (4, 3, 'bread'),    # Move the bread from Box 4 to Box 3
    (3, None, 'computer'),  # Remove the computer from Box 3
    (3, None, 'ring'),  # Remove the ring from Box 3
    (None, 3, 'painting'),  # Put the painting into Box 3
    (5, None, 'beer'),  # Remove the beer from Box 5
    (5, None, 'bone'),  # Remove the bone from Box 5
    (5, None, 'plate'),  # Remove the plate from Box 5
    (None, 5, 'sheet'),  # Put the sheet into Box 5
    (None, 5, 'brick'),  # Put the brick into Box 5
    (1, None, 'file'),  # Remove the file from Box 1
    (4, None, 'crown'),  # Remove the crown from Box 4
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