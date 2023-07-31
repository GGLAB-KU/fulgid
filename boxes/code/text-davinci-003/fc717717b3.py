# Initialize the boxes
boxes = {
    0: ['computer', 'machine'],
    1: [],
    2: [],
    3: ['suit'],
    4: ['apple', 'clock', 'leaf'],
    5: ['car', 'cross'],
    6: ['plate'],
}

# Define the moves
moves = [
    (6, 2, 'plate'),        # Move the plate from Box 6 to Box 2
    (None, 3, 'stone'),     # Put the stone into Box 3
    (4, 2, 'clock'),        # Move the clock from Box 4 to Box 2
    (4, 2, 'leaf'),         # Move the leaf from Box 4 to Box 2
    (None, 3, 'branch'),    # Put the branch into Box 3
    (2, None, 'clock'),     # Remove the clock from Box 2
    (4, None, 'apple'),     # Remove the apple from Box 4
    (3, 6, 'stone'),        # Move the stone from Box 3 to Box 6
    (6, 2, 'stone'),        # Move the stone from Box 6 to Box 2
    (None, 4, 'document'),  # Put the document into Box 4
    (3, 6, 'branch'),       # Move the branch from Box 3 to Box 6
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