# Initialize the boxes
boxes = {
    0: ['disk'],
    1: ['hat'],
    2: ['bottle', 'plane', 'wire'],
    3: ['bus', 'crown'],
    4: ['tie', 'train'],
    5: ['creature', 'glass', 'stone'],
    6: ['bowl', 'shirt', 'watch'],
}

# Define the moves
moves = [
    (6, None, 'bowl'),       # Remove the bowl from Box 6
    (6, None, 'watch'),      # Remove the watch from Box 6
    (2, 0, 'plane'),         # Move the plane from Box 2 to Box 0
    (2, 0, 'wire'),          # Move the wire from Box 2 to Box 0
    (0, None, 'disk'),       # Remove the disk from Box 0
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