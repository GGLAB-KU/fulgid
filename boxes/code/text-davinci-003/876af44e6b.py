# Initialize the boxes
boxes = {
    0: ['book'],
    1: ['branch', 'key'],
    2: [],
    3: [],
    4: ['bottle', 'brick', 'computer'],
    5: ['stone'],
    6: ['block', 'letter', 'meat'],
}

# Define the moves
moves = [
    (0, None, 'book'),       # Remove the book from Box 0
    (1, 5, 'branch'),         # Move the branch from Box 1 to Box 5
    (1, None, 'key'),        # Remove the key from Box 1
    (None, 3, 'egg'),        # Put the egg into Box 3
    (None, 3, 'seed'),       # Put the seed into Box 3
    (3, 1, 'egg'),           # Move the egg from Box 3 to Box 1
    (None, 5, 'clock'),      # Put the clock into Box 5
    (4, 1, 'bottle'),        # Move the bottle from Box 4 to Box 1
    (4, 1, 'brick'),         # Move the brick from Box 4 to Box 1
    (5, None, 'stone'),      # Remove the stone from Box 5
    (1, None, 'bottle')      # Remove the bottle from Box 1
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