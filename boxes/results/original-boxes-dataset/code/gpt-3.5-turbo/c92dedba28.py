# Initialize the boxes
boxes = {
    0: ['coffee', 'tissue'],
    1: ['camera', 'dress'],
    2: ['leaf'],
    3: ['apple', 'book'],
    4: ['key', 'radio', 'tape'],
    5: ['beer', 'crown', 'suit'],
    6: ['brain', 'paper', 'plate'],
}

# Define the moves
moves = [
    (3, None, 'book'),       # Remove the book from Box 3
    (6, 3, 'brain'),         # Move the brain from Box 6 to Box 3
    (6, 3, 'plate'),         # Move the plate from Box 6 to Box 3
    (3, None, 'brain'),      # Remove the brain from Box 3
    (5, None, 'crown'),      # Remove the crown from Box 5
    (1, None, 'dress'),      # Remove the dress from Box 1
    (0, 1, 'tissue'),        # Move the tissue from Box 0 to Box 1
    (3, None, 'apple'),      # Remove the apple from Box 3
    (6, None, 'paper'),      # Remove the paper from Box 6
    (3, None, 'plate'),      # Remove the plate from Box 3
    (None, 3, 'engine'),     # Put the engine into Box 3
    (2, None, 'leaf'),       # Remove the leaf from Box 2
    (None, 6, 'fig')         # Put the fig into Box 6
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