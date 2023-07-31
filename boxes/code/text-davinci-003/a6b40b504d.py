# Initialize the boxes
boxes = {
    0: ['dish', 'document'],
    1: ['coffee', 'ice'],
    2: ['branch', 'ring'],
    3: [],
    4: ['cream', 'meat', 'plant'],
    5: ['bus', 'sheet'],
    6: ['bottle', 'disk', 'phone'],
}

# Define the moves
moves = [
    (0, 1, 'dish'),         # Move the dish from Box 0 to Box 1
    (2, None, 'branch'),    # Remove the branch from Box 2
    (2, None, 'ring'),      # Remove the ring from Box 2
    (None, 3, 'creature'),  # Put the creature into Box 3
    (3, 0, 'ring'),         # Move the ring from Box 3 to Box 0
    (0, None, 'ring'),      # Remove the ring from Box 0
    (None, 0, 'camera'),    # Put the camera into Box 0
    (None, 0, 'fan'),       # Put the fan into Box 0
    (6, None, 'disk'),      # Remove the disk from Box 6
    (6, None, 'phone'),     # Remove the phone from Box 6
    (0, None, 'fan'),       # Remove the fan from Box 0
    (3, 0, 'creature'),     # Move the creature from Box 3 to Box 0
    (None, 5, 'fish'),      # Put the fish into Box 5
    (5, 6, 'bus'),          # Move the bus from Box 5 to Box 6
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