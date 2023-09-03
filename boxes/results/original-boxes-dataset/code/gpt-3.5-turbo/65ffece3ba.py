# Initialize the boxes
boxes = {
    0: ['mirror', 'plane'],
    1: ['cheese', 'disk', 'tissue'],
    2: ['pipe', 'watch'],
    3: ['flower', 'shirt'],
    4: ['book', 'tea'],
    5: ['drug'],
    6: ['ice'],
}

# Define the moves
moves = [
    (None, 6, 'leaf'),       # Put the leaf into Box 6
    (3, None, 'flower'),     # Remove the flower from Box 3
    (3, None, 'shirt'),      # Remove the shirt from Box 3
    (6, None, 'ice'),        # Remove the ice from Box 6
    (6, None, 'leaf'),       # Remove the leaf from Box 6
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