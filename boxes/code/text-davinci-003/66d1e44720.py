# Initialize the boxes
boxes = {
    0: ['bowl', 'glass', 'ring'],
    1: ['computer', 'disk'],
    2: ['ice'],
    3: ['coat', 'file', 'painting'],
    4: ['bomb'],
    5: ['bus', 'magazine', 'meat'],
    6: ['cigarette', 'seed'],
}

# Define the moves
moves = [
    (0, None, 'bowl'),         # Remove the bowl from Box 0
    (0, None, 'glass'),        # Remove the glass from Box 0
    (0, None, 'ring'),         # Remove the ring from Box 0
    (1, 0, 'disk'),            # Move the disk from Box 1 to Box 0
    (2, 4, 'ice'),             # Move the ice from Box 2 to Box 4
    (None, 0, 'machine'),      # Put the machine into Box 0
    (None, 0, 'shell'),        # Put the shell into Box 0
    (3, None, 'file'),         # Remove the file from Box 3
    (3, None, 'painting'),     # Remove the painting from Box 3
    (None, 3, 'coffee'),       # Put the coffee into Box 3
    (None, 3, 'fish'),         # Put the fish into Box 3
    (5, 1, 'magazine'),        # Move the magazine from Box 5 to Box 1
    (None, 1, 'engine'),       # Put the engine into Box 1
    (0, 2, 'disk'),            # Move the disk from Box 0 to Box 2
    (0, 2, 'machine'),         # Move the machine from Box 0 to Box 2
    (0, 2, 'shell'),           # Move the shell from Box 0 to Box 2
    (None, 4, 'apple')         # Put the apple into Box 4
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