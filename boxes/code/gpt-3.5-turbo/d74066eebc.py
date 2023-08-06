# Initialize the boxes
boxes = {
    0: ['egg'],
    1: ['apple'],
    2: ['radio', 'tea', 'watch'],
    3: ['cake'],
    4: ['boat', 'clock', 'fan'],
    5: ['disk'],
    6: ['sheet'],
}

# Define the moves
moves = [
    (3, None, 'cake'),       # Remove the cake from Box 3
    (0, None, 'egg'),        # Remove the egg from Box 0
    (None, 0, 'fig'),        # Put the fig into Box 0
    (4, None, 'clock'),      # Remove the clock from Box 4
    (4, None, 'fan'),        # Remove the fan from Box 4
    (4, None, 'boat'),       # Remove the boat from Box 4
    (1, 3, 'apple'),         # Move the apple from Box 1 to Box 3
    (0, None, 'fig'),        # Remove the fig from Box 0
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