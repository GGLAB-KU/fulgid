# Initialize the boxes
boxes = {
    0: ['pipe'],
    1: ['fan'],
    2: ['leaf'],
    3: ['flower', 'magazine'],
    4: ['file', 'milk', 'television'],
    5: ['cake', 'plane', 'string'],
    6: ['bus', 'computer'],
}

# Define the moves
moves = [
    (3, None, 'flower'),    # Remove the flower from Box 3
    (3, None, 'magazine'),  # Remove the magazine from Box 3
    (1, None, 'fan'),       # Remove the fan from Box 1
    (5, 2, 'cake'),         # Move the cake from Box 5 to Box 2
    (5, 2, 'string'),       # Move the string from Box 5 to Box 2
    (0, 1, 'pipe'),         # Move the pipe from Box 0 to Box 1
    (4, 1, 'milk'),         # Move the milk from Box 4 to Box 1
    (None, 1, 'knife'),     # Put the knife into Box 1
    (1, None, 'knife'),     # Remove the knife from Box 1
    (1, None, 'pipe'),      # Remove the pipe from Box 1
    (None, 3, 'camera'),    # Put the camera into Box 3
    (None, 5, 'car'),       # Put the car into Box 5
    (None, 5, 'tea'),       # Put the tea into Box 5
    (6, None, 'bus'),       # Remove the bus from Box 6
    (None, 1, 'ice'),       # Put the ice into Box 1
    (4, 3, 'file'),         # Move the file from Box 4 to Box 3
    (4, 3, 'television')    # Move the television from Box 4 to Box 3
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