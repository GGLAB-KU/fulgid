# Initialize the boxes
boxes = {
    0: ['boat'],
    1: ['document', 'ice', 'mirror'],
    2: ['branch', 'cash', 'seed'],
    3: ['shell'],
    4: [],
    5: ['block', 'bottle', 'dish'],
    6: [],
}

# Define the moves
moves = [
    (0, 6, 'boat'),         # Move the boat from Box 0 to Box 6
    (6, 4, 'boat'),         # Move the boat from Box 6 to Box 4
    (3, None, 'shell'),     # Remove the shell from Box 3
    (1, 4, 'document'),     # Move the document from Box 1 to Box 4
    (1, None, 'mirror'),    # Remove the mirror from Box 1
    (4, None, 'document'),  # Remove the document from Box 4
    (None, 3, 'wire'),      # Put the wire into Box 3
    (2, 1, 'branch'),       # Move the branch from Box 2 to Box 1
    (2, 1, 'seed'),         # Move the seed from Box 2 to Box 1
    (1, None, 'ice'),       # Remove the ice from Box 1
    (1, None, 'seed'),      # Remove the seed from Box 1
    (None, 6, 'cheese'),    # Put the cheese into Box 6
    (3, None, 'wire'),      # Remove the wire from Box 3
    (4, 0, 'boat'),         # Move the boat from Box 4 to Box 0
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