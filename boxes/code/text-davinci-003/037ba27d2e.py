# Initialize the boxes
boxes = {
    0: ['wheel'],
    1: ['boot'],
    2: ['tea'],
    3: ['crown', 'drug', 'seed'],
    4: ['cake', 'medicine'],
    5: ['bottle', 'fish'],
    6: ['egg', 'meat', 'mirror'],
}

# Define the moves
moves = [
    (2, 0, 'tea'),       # Move the tea from Box 2 to Box 0
    (6, None, 'meat'),   # Remove the meat from Box 6
    (6, None, 'mirror'), # Remove the mirror from Box 6
    (0, 1, 'tea'),       # Move the tea from Box 0 to Box 1
    (0, 1, 'wheel'),     # Move the wheel from Box 0 to Box 1
    (6, None, 'egg'),    # Remove the egg from Box 6
    (4, None, 'cake'),   # Remove the cake from Box 4
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