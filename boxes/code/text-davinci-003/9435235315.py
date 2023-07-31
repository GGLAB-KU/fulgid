# Initialize the boxes
boxes = {
    0: ['meat', 'tea'],
    1: ['bottle', 'computer', 'disk'],
    2: ['file'],
    3: ['boot', 'drug', 'jacket'],
    4: ['cross'],
    5: ['book', 'cigarette', 'fig'],
    6: ['car', 'watch'],
}

# Define the moves
moves = [
    (4, 0, 'cross'),   # Move the cross from Box 4 to Box 0
    (1, None, 'bottle')   # Remove the bottle from Box 1
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