# Initialize the boxes
boxes = {
    0: ['cheese', 'cross', 'disk'],
    1: ['bag'],
    2: [],
    3: ['ball', 'glass', 'seed'],
    4: ['cash', 'drug', 'stone'],
    5: ['suit'],
    6: [],
}

# Define the moves
moves = [
    (0, 1, 'cheese'),    # Move the cheese from Box 0 to Box 1
    (0, 1, 'disk'),      # Move the disk from Box 0 to Box 1
    (None, 5, 'cake'),   # Put the cake into Box 5
    (None, 2, 'meat'),   # Put the meat into Box 2
    (None, 0, 'picture'),# Put the picture into Box 0
    (1, None, 'bag'),    # Remove the bag from Box 1
    (0, None, 'cross'),  # Remove the cross from Box 0
    (0, None, 'picture'),# Remove the picture from Box 0
    (2, None, 'meat'),   # Remove the meat from Box 2
    (1, 0, 'disk'),      # Move the disk from Box 1 to Box 0
    (None, 6, 'apple'),  # Put the apple into Box 6
    (None, 6, 'camera'), # Put the camera into Box 6
    (None, 6, 'dish'),   # Put the dish into Box 6
    (1, 0, 'cheese'),    # Move the cheese from Box 1 to Box 0
    (None, 2, 'flower'), # Put the flower into Box 2
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