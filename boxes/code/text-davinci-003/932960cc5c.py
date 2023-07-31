# Initialize the boxes
boxes = {
    0: ['camera', 'chemical', 'plant'],
    1: [],
    2: ['newspaper', 'tea', 'wire'],
    3: [],
    4: ['branch', 'painting', 'shell'],
    5: ['cake', 'disk', 'machine'],
    6: ['cross', 'phone', 'picture'],
}

# Define the moves
moves = [
    (0, None, 'chemical'),     # Remove the chemical from Box 0
    (0, None, 'plant'),        # Remove the plant from Box 0
    (0, None, 'camera'),       # Remove the camera from Box 0
    (4, None, 'shell'),        # Remove the shell from Box 4
    (2, None, 'newspaper'),    # Remove the newspaper from Box 2
    (5, 4, 'disk'),            # Move the disk from Box 5 to Box 4
    (0, 4, 'disk'),            # Move the disk from Box 0 to Box 4
    (0, 4, 'painting'),        # Move the painting from Box 0 to Box 4
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