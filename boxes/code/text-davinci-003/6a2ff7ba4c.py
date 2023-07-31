# Initialize the boxes
boxes = {
    0: ['computer', 'machine'],
    1: [],
    2: [],
    3: ['suit'],
    4: ['apple', 'clock', 'leaf'],
    5: ['car', 'cross'],
    6: ['plate'],
}

# Define the moves
moves = [
    (6, 2, 'plate'),    # Move the plate from Box 6 to Box 2
    (None, 3, 'stone'),  # Put the stone into Box 3
    (4, 2, 'clock'),     # Move the clock from Box 4 to Box 2
    (4, 2, 'leaf')       # Move the leaf from Box 4 to Box 2
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