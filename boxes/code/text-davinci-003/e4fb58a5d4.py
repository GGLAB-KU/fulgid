# Initialize the boxes
boxes = {
    0: [],
    1: ['block', 'cheese', 'note'],
    2: ['cake', 'cross'],
    3: [],
    4: [],
    5: ['clock'],
    6: ['bottle', 'flower'],
}

# Define the moves
moves = [
    (2, 3, 'cake'),         # Move the cake from Box 2 to Box 3
    (2, None, 'cross'),     # Remove the cross from Box 2
    (6, 4, 'flower'),       # Move the flower from Box 6 to Box 4
    (6, 0, 'bottle'),       # Move the bottle from Box 6 to Box 0
    (None, 4, 'book'),      # Put the book into Box 4
    (0, None, 'bottle'),    # Remove the bottle from Box 0
    (3, 2, 'cake'),         # Move the cake from Box 3 to Box 2
    (4, 6, 'flower'),       # Move the flower from Box 4 to Box 6
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