# Initialize the boxes
boxes = {
    0: ['key', 'ring', 'train'],
    1: ['dish', 'tape', 'wire'],
    2: ['bottle', 'jacket'],
    3: ['bag', 'brick', 'plant'],
    4: ['car', 'flower'],
    5: ['boat'],
    6: ['boot', 'coat', 'sheet'],
}

# Define the moves
moves = [
    (0, 5, 'key'),         # Move the key from Box 0 to Box 5
    (0, 5, 'train'),       # Move the train from Box 0 to Box 5
    (3, None, 'bag'),      # Remove the bag from Box 3
    (3, None, 'brick'),    # Remove the brick from Box 3
    (None, 0, 'pipe'),     # Put the pipe into Box 0
    (2, None, 'jacket'),   # Remove the jacket from Box 2
    (2, None, 'bottle'),   # Remove the bottle from Box 2
    (4, None, 'car'),      # Remove the car from Box 4
    (4, None, 'flower'),   # Remove the flower from Box 4
    (6, 4, 'coat'),        # Move the coat from Box 6 to Box 4
    (6, 4, 'sheet'),       # Move the sheet from Box 6 to Box 4
    (None, 2, 'picture'),  # Put the picture into Box 2
    (4, None, 'sheet'),    # Remove the sheet from Box 4
    (2, None, 'picture'),  # Remove the picture from Box 2
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