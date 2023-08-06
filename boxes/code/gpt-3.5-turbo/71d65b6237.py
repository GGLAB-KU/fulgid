# Initialize the boxes
boxes = {
    0: ['book', 'brick'],
    1: ['bus', 'crown', 'plant'],
    2: ['apple', 'drug', 'wire'],
    3: ['file'],
    4: ['game'],
    5: ['paper', 'ring'],
    6: ['milk', 'watch'],
}

# Define the moves
moves = [
    (1, None, 'bus'),       # Remove the bus from Box 1
    (None, 3, 'painting'),  # Put the painting into Box 3
    (4, None, 'game'),      # Remove the game from Box 4
    (1, None, 'plant'),     # Remove the plant from Box 1
    (6, None, 'watch'),     # Remove the watch from Box 6
    (1, None, 'crown'),     # Remove the crown from Box 1
    (5, None, 'paper'),     # Remove the paper from Box 5
    (5, None, 'ring'),      # Remove the ring from Box 5
    (0, None, 'book'),      # Remove the book from Box 0
    (0, None, 'brick'),     # Remove the brick from Box 0
    (6, None, 'milk'),      # Remove the milk from Box 6
    (3, None, 'file'),      # Remove the file from Box 3
    (3, 6, 'painting'),     # Move the painting from Box 3 to Box 6
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