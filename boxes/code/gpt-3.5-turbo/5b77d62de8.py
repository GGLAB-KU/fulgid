# Initialize the boxes
boxes = {
    0: ['seed'],
    1: ['cake', 'document', 'television'],
    2: ['glass', 'plane'],
    3: [],
    4: ['bone', 'cheese', 'coffee'],
    5: ['ball'],
    6: ['book', 'disk', 'tissue'],
}

# Define the moves
moves = [
    (None, 5, 'shell'),         # Put the shell into Box 5
    (6, 0, 'disk'),             # Move the disk from Box 6 to Box 0
    (None, 0, 'map'),           # Put the map into Box 0
    (None, 6, 'flower'),        # Put the flower into Box 6
    (1, 3, 'document'),         # Move the document from Box 1 to Box 3
    (1, 3, 'television'),       # Move the television from Box 1 to Box 3
    (5, None, 'shell'),         # Remove the shell from Box 5
    (4, None, 'bone'),          # Remove the bone from Box 4
    (4, None, 'coffee'),        # Remove the coffee from Box 4
    (2, 1, 'glass'),            # Move the glass from Box 2 to Box 1
    (2, 1, 'plane'),            # Move the plane from Box 2 to Box 1
    (3, None, 'document'),      # Remove the document from Box 3
    (3, None, 'television'),    # Remove the television from Box 3
    (None, 5, 'paper'),         # Put the paper into Box 5
    (None, 5, 'television'),    # Put the television into Box 5
    (4, 3, 'cheese'),           # Move the cheese from Box 4 to Box 3
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