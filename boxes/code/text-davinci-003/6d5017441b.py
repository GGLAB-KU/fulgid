# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['camera', 'tape'],
    3: ['dish'],
    4: ['cake', 'map', 'plate'],
    5: ['cigarette', 'painting', 'shoe'],
    6: ['brick', 'magazine'],
}

# Define the moves
moves = [
    (5, None, 'cigarette'),     # Remove the cigarette from Box 5
    (None, 1, 'cream'),         # Put the cream into Box 1
    (1, 6, 'cream'),            # Move the cream from Box 1 to Box 6
    (4, None, 'map'),           # Remove the map from Box 4
    (4, None, 'plate'),         # Remove the plate from Box 4
    (6, 0, 'cream'),            # Move the cream from Box 6 to Box 0
    (6, 0, 'magazine'),         # Move the magazine from Box 6 to Box 0
    (4, None, 'cake'),          # Remove the cake from Box 4
    (0, None, 'cream'),         # Remove the cream from Box 0
    (2, None, 'camera'),        # Remove the camera from Box 2
    (2, None, 'tape'),          # Remove the tape from Box 2
    (0, 5, 'magazine'),         # Move the magazine from Box 0 to Box 5
    (None, 4, 'shell'),         # Put the shell into Box 4
    (5, 4, 'magazine')          # Move the magazine from Box 5 to Box 4
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