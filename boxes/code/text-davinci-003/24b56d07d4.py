# Initialize the boxes
boxes = {
    0: ['machine'],
    1: ['phone'],
    2: ['apple', 'brain', 'guitar'],
    3: ['camera', 'picture', 'ticket'],
    4: ['shoe', 'suit', 'tape'],
    5: ['book', 'branch', 'newspaper'],
    6: ['bus', 'key'],
}

# Define the moves
moves = [
    (2, None, 'brain'),       # Remove the brain from Box 2
    (4, None, 'shoe'),        # Remove the shoe from Box 4
    (6, 0, 'key'),            # Move the key from Box 6 to Box 0
    (3, None, 'camera'),      # Remove the camera from Box 3
    (3, None, 'ticket'),      # Remove the ticket from Box 3
    (0, 1, 'machine'),        # Move the machine from Box 0 to Box 1
    (4, None, 'suit'),        # Remove the suit from Box 4
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