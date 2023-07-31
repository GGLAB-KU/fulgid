# Initialize the boxes
boxes = {
    0: ['car', 'engine', 'jacket'],
    1: [],
    2: ['cake'],
    3: ['bowl', 'fig', 'sheet'],
    4: ['computer', 'creature', 'string'],
    5: [],
    6: [],
}

# Define the moves
moves = [
    (4, 1, 'creature'),    # Move the creature from Box 4 to Box 1
    (4, 1, 'string'),      # Move the string from Box 4 to Box 1
    (0, 6, 'engine'),      # Move the engine from Box 0 to Box 6
    (3, 6, 'bowl'),        # Move the bowl from Box 3 to Box 6
    (3, 6, 'fig'),         # Move the fig from Box 3 to Box 6
    (2, None, 'cake'),     # Remove the cake from Box 2
    (1, 2, 'creature'),    # Move the creature from Box 1 to Box 2
    (3, 4, 'sheet'),       # Move the sheet from Box 3 to Box 4
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