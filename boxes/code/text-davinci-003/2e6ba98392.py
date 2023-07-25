# Initialize the boxes
boxes = {
    0: ['cross', 'egg', 'gift'],
    1: [],
    2: ['crown', 'fig'],
    3: ['brain', 'dish'],
    4: ['computer', 'fish', 'meat'],
    5: ['beer', 'cheese', 'seed'],
    6: ['bell', 'document', 'wire'],
}

# Define the moves
moves = [
    (4, None, 'fish'),       # Remove the fish from Box 4
    (4, None, 'meat'),       # Remove the meat from Box 4
    (6, 1, 'document'),      # Move the document from Box 6 to Box 1
    (1, 4, 'document'),      # Move the document from Box 1 to Box 4
    (0, None, 'cross'),      # Remove the cross from Box 0
    (0, None, 'gift'),       # Remove the gift from Box 0
    (0, None, 'egg'),        # Remove the egg from Box 0
    (None, 4, 'gift'),       # Put the gift into Box 4
    (2, 6, 'crown'),         # Move the crown from Box 2 to Box 6
    (2, None, 'tissue'),     # Put the tissue into Box 2
    (3, None, 'brain'),      # Remove the brain from Box 3
    (6, None, 'bell'),       # Remove the bell from Box 6
    (2, None, 'tissue'),     # Remove the tissue from Box 2
    (6, 0, 'wire'),          # Move the wire from Box 6 to Box 0
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