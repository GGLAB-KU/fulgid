# Initialize the boxes
boxes = {
    0: ['branch', 'ticket'],
    1: [],
    2: ['bag', 'brain', 'knife'],
    3: ['file', 'milk'],
    4: ['block', 'watch'],
    5: [],
    6: ['key'],
}

# Define the moves
moves = [
    (4, None, 'watch'),       # Remove the watch from Box 4
    (2, None, 'bag'),         # Remove the bag from Box 2
    (2, None, 'brain'),       # Remove the brain from Box 2
    (2, None, 'knife'),       # Remove the knife from Box 2
    (6, None, 'key'),         # Remove the key from Box 6
    (3, 0, 'file'),           # Move the file from Box 3 to Box 0
    (3, 4, 'milk'),           # Move the milk from Box 3 to Box 4
    (None, 5, 'picture'),     # Put the picture into Box 5
    (4, None, 'block'),       # Remove the block from Box 4
    (0, 6, 'ticket'),         # Move the ticket from Box 0 to Box 6
    (None, 3, 'cheese'),      # Put the cheese into Box 3
    (0, None, 'branch'),      # Remove the branch from Box 0
    (0, None, 'file'),        # Remove the file from Box 0
    (5, 2, 'picture'),        # Move the picture from Box 5 to Box 2
    (None, 1, 'brick')        # Put the brick into Box 1
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