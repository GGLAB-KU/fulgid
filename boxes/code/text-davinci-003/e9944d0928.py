# Initialize the boxes
boxes = {
    0: ['bottle'],
    1: ['mirror', 'rock', 'tie'],
    2: ['bowl', 'camera', 'file'],
    3: ['flower'],
    4: ['creature', 'shell'],
    5: ['bag', 'note'],
    6: [],
}

# Define the moves
moves = [
    (0, None, 'bottle'),    # Remove the bottle from Box 0
    (3, None, 'flower'),    # Remove the flower from Box 3
    (None, 6, 'wheel'),     # Put the wheel into Box 6
    (None, 5, 'book'),      # Put the book into Box 5
    (6, None, 'wheel')      # Remove the wheel from Box 6
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