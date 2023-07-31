# Initialize the boxes
boxes = {
    0: ['clock', 'pot', 'tea'],
    1: ['apple', 'bone', 'plate'],
    2: ['watch'],
    3: ['cheese'],
    4: ['newspaper', 'painting'],
    5: [],
    6: ['beer', 'cup'],
}

# Define the moves
moves = [
    (2, None, 'watch'),     # Remove the watch from Box 2
    (3, None, 'cheese'),    # Remove the cheese from Box 3
    (None, 2, 'bottle'),    # Put the bottle into Box 2
    (None, 2, 'letter')     # Put the letter into Box 2
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