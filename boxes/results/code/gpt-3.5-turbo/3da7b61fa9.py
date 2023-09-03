# Initialize the boxes
boxes = {
    0: ['coffee', 'engine', 'fan'],
    1: ['cash', 'ice'],
    2: ['cheese'],
    3: ['bell', 'crown', 'picture'],
    4: ['drink'],
    5: ['machine'],
    6: ['letter'],
}

# Define the moves
moves = [
    (None, 5, 'egg'),       # Put the egg into Box 5
    (2, 4, 'cheese'),       # Move the cheese from Box 2 to Box 4
    (3, None, 'bell'),      # Remove the bell from Box 3
    (0, None, 'engine'),    # Remove the engine from Box 0
    (0, 6, 'coffee'),       # Move the coffee from Box 0 to Box 6
    (None, 3, 'document'),  # Put the document into Box 3
    (6, None, 'coffee'),    # Remove the coffee from Box 6
    (6, None, 'letter'),    # Remove the letter from Box 6
    (5, 2, 'egg'),          # Move the egg from Box 5 to Box 2
    (4, 6, 'cheese'),       # Move the cheese from Box 4 to Box 6
    (4, 6, 'drink'),        # Move the drink from Box 4 to Box 6
    (2, None, 'egg'),       # Remove the egg from Box 2
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