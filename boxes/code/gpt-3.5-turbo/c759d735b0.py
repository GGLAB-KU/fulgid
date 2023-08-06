# Initialize the boxes
boxes = {
    0: ['dress', 'flower', 'map'],
    1: ['cup'],
    2: ['bell', 'egg', 'jacket'],
    3: ['cream', 'document'],
    4: ['cross', 'fan'],
    5: [],
    6: ['cake', 'plane'],
}

# Define the moves
moves = [
    (0, 1, 'shoe'),         # Put the shoe into Box 1
    (6, 5, 'plane'),        # Move the plane from Box 6 to Box 5
    (3, 6, 'document'),     # Move the document from Box 3 to Box 6
    (2, 3, 'bell'),         # Move the bell from Box 2 to Box 3
    (2, 3, 'jacket'),       # Move the jacket from Box 2 to Box 3
    (3, 2, 'bell'),         # Move the bell from Box 3 to Box 2
    (3, 2, 'jacket'),       # Move the jacket from Box 3 to Box 2
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