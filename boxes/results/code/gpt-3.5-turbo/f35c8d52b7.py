# Initialize the boxes
boxes = {
    0: [],
    1: ['dish', 'television', 'tie'],
    2: [],
    3: ['bus'],
    4: [],
    5: ['medicine', 'plant', 'sheet'],
    6: ['pipe'],
}

# Define the moves
moves = [
    (3, None, 'bus'),       # Remove the bus from Box 3
    (6, 2, 'pipe'),         # Move the pipe from Box 6 to Box 2
    (5, None, 'medicine'),  # Remove the medicine from Box 5
    (2, 4, 'pipe'),         # Move the pipe from Box 2 to Box 4
    (5, 4, 'plant'),        # Move the plant from Box 5 to Box 4
    (5, None, 'sheet'),     # Remove the sheet from Box 5
    (None, 0, 'hat'),       # Put the hat into Box 0
    (None, 0, 'leaf')       # Put the leaf into Box 0
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