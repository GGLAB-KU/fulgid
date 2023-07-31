# Initialize the boxes
boxes = {
    0: ['apple', 'leaf', 'milk'],
    1: ['beer', 'branch', 'pipe'],
    2: ['bread', 'clock'],
    3: ['bell', 'watch'],
    4: ['drink', 'egg'],
    5: ['chemical', 'fish', 'key'],
    6: ['camera'],
}

# Define the moves
moves = [
    (6, None, 'camera'),       # Remove the camera from Box 6
    (3, None, 'watch'),        # Remove the watch from Box 3
    (2, None, 'bread'),        # Remove the bread from Box 2
    (2, None, 'clock'),        # Remove the clock from Box 2
    (1, 3, 'branch'),          # Move the branch from Box 1 to Box 3
    (1, 3, 'pipe'),            # Move the pipe from Box 1 to Box 3
    (1, 6, 'beer'),            # Move the beer from Box 1 to Box 6
    (6, 1, 'beer'),            # Move the beer from Box 6 to Box 1
    (0, None, 'milk'),         # Remove the milk from Box 0
    (None, 1, 'plate'),        # Put the plate into Box 1
    (3, 6, 'bell'),            # Move the bell from Box 3 to Box 6
    (3, 6, 'pipe'),            # Move the pipe from Box 3 to Box 6
    (None, 6, 'jacket'),       # Put the jacket into Box 6
    (None, 3, 'clock'),        # Put the clock into Box 3
    (None, 2, 'ticket')        # Put the ticket into Box 2
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