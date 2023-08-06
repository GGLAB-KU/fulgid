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
    (4, 0, 'disk'),            # Move the disk from Box 4 to Box 0
    (4, 0, 'painting'),        # Move the painting from Box 4 to Box 0
    (6, None, 'cross'),        # Remove the cross from Box 6
    (6, None, 'picture'),      # Remove the picture from Box 6
    (6, None, 'phone'),        # Remove the phone from Box 6
    (2, None, 'wire'),         # Remove the wire from Box 2
    (2, None, 'tea'),          # Remove the tea from Box 2
    (None, 2, 'flower'),       # Put the flower into Box 2
    (None, 2, 'jacket'),       # Put the jacket into Box 2
    (None, 2, 'paper')         # Put the paper into Box 2
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