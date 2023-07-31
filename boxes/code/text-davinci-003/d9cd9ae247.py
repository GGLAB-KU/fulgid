# Initialize the boxes
boxes = {
    0: ['painting'],
    1: ['coat', 'ring', 'tie'],
    2: ['camera', 'file', 'milk'],
    3: ['bone', 'train'],
    4: ['magazine'],
    5: ['bomb', 'game'],
    6: ['brick', 'cigarette', 'disk'],
}

# Define the moves
moves = [
    (2, None, 'file'),       # Remove the file from Box 2
    (6, 5, 'brick'),         # Move the brick from Box 6 to Box 5
    (4, None, 'magazine'),   # Remove the magazine from Box 4
    (2, None, 'camera'),     # Remove the camera from Box 2
    (2, 4, 'milk'),          # Move the milk from Box 2 to Box 4
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