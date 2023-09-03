# Initialize the boxes
boxes = {
    0: ['block', 'dress'],
    1: [],
    2: ['ball', 'key', 'tape'],
    3: ['bomb'],
    4: [],
    5: ['engine', 'leaf'],
    6: ['card', 'cup'],
}

# Define the moves
moves = [
    (2, None, 'ball'),    # Remove the ball from Box 2
    (None, 4, 'brain'),    # Put the brain into Box 4
    (4, 3, 'brain'),       # Move the brain from Box 4 to Box 3
    (2, 1, 'key'),         # Move the key from Box 2 to Box 1
    (None, 5, 'book'),     # Put the book into Box 5
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