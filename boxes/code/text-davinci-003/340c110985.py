# Initialize the boxes
boxes = {
    0: ['beer', 'bread', 'dress'],
    1: ['apple'],
    2: ['ball', 'pipe', 'watch'],
    3: ['clock', 'crown'],
    4: ['brain', 'fan', 'tissue'],
    5: ['glass', 'tea'],
    6: ['gift', 'television'],
}

# Define the moves
moves = [
    (2, None, 'watch'),     # Remove the watch from Box 2
    (1, 2, 'apple'),        # Move the apple from Box 1 to Box 2
    (None, 1, 'branch'),    # Put the branch into Box 1
    (2, None, 'apple'),     # Remove the apple from Box 2
    (2, None, 'pipe'),      # Remove the pipe from Box 2
    (3, None, 'crown'),     # Remove the crown from Box 3
    (None, 5, 'fig'),       # Put the fig into Box 5
    (2, None, 'ball'),      # Remove the ball from Box 2
    (3, None, 'clock'),     # Remove the clock from Box 3
    (1, 2, 'branch'),       # Move the branch from Box 1 to Box 2
    (None, 6, 'magazine'),  # Put the magazine into Box 6
    (None, 2, 'picture')    # Put the picture into Box 2
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