# Initialize the boxes
boxes = {
    0: [],
    1: ['chemical'],
    2: ['brain', 'paper'],
    3: ['bread'],
    4: ['cheese', 'cross'],
    5: ['block'],
    6: ['bone', 'dish', 'plate'],
}

# Define the moves
moves = [
    (None, 3, 'apple'),     # Put the apple into Box 3
    (None, 3, 'mirror'),    # Put the mirror into Box 3
    (2, 0, 'paper'),        # Move the paper from Box 2 to Box 0
    (6, None, 'bone'),      # Remove the bone from Box 6
    (4, None, 'cheese'),    # Remove the cheese from Box 4
    (4, None, 'cross'),     # Remove the cross from Box 4
    (None, 1, 'bomb'),      # Put the bomb into Box 1
    (3, None, 'bread'),     # Remove the bread from Box 3
    (3, None, 'mirror'),    # Remove the mirror from Box 3
    (6, None, 'dish'),      # Remove the dish from Box 6
    (5, 4, 'block'),        # Move the block from Box 5 to Box 4
    (1, None, 'bomb'),      # Remove the bomb from Box 1
    (1, None, 'chemical')   # Remove the chemical from Box 1
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