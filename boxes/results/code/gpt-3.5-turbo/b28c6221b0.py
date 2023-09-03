# Initialize the boxes
boxes = {
    0: ['crown', 'picture'],
    1: ['bone', 'cheese', 'clock'],
    2: ['egg', 'gift', 'medicine'],
    3: ['letter'],
    4: [],
    5: ['flower'],
    6: ['computer'],
}

# Define the moves
moves = [
    (2, None, 'egg'),       # Remove the egg from Box 2
    (2, None, 'gift'),      # Remove the gift from Box 2
    (2, None, 'medicine'),  # Remove the medicine from Box 2
    (1, 4, 'bone'),         # Move the bone from Box 1 to Box 4
    (1, 4, 'cheese'),       # Move the cheese from Box 1 to Box 4
    (1, 4, 'clock'),        # Move the clock from Box 1 to Box 4
    (5, 3, 'flower'),       # Move the flower from Box 5 to Box 3
    (None, 6, 'boot'),      # Put the boot into Box 6
    (None, 6, 'plane'),     # Put the plane into Box 6
    (4, None, 'bone'),      # Remove the bone from Box 4
    (4, None, 'cheese'),    # Remove the cheese from Box 4
    (6, 4, 'boot'),         # Move the boot from Box 6 to Box 4
    (0, 3, 'picture'),      # Move the picture from Box 0 to Box 3
    (6, 4, 'plane')         # Move the plane from Box 6 to Box 4
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