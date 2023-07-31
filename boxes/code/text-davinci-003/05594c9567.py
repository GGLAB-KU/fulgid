# Initialize the boxes
boxes = {
    0: [],
    1: ['plant', 'seed'],
    2: [],
    3: ['crown', 'newspaper', 'television'],
    4: [],
    5: ['bag', 'hat', 'picture'],
    6: ['bottle', 'document', 'pot'],
}

# Define the moves
moves = [
    (None, 2, 'branch'),       # Put the branch into Box 2
    (1, None, 'plant'),        # Remove the plant from Box 1
    (1, None, 'seed'),         # Remove the seed from Box 1
    (6, None, 'bottle'),       # Remove the bottle from Box 6
    (6, 1, 'pot'),             # Move the pot from Box 6 to Box 1
    (1, 6, 'pot'),             # Move the pot from Box 1 to Box 6
    (6, 0, 'document'),        # Move the document from Box 6 to Box 0
    (6, 0, 'pot'),             # Move the pot from Box 6 to Box 0
    (2, None, 'branch'),       # Remove the branch from Box 2
    (0, 1, 'document'),        # Move the document from Box 0 to Box 1
    (0, None, 'document'),     # Remove the document from Box 0
    (5, 1, 'hat'),             # Move the hat from Box 5 to Box 1
    (3, 0, 'crown'),           # Move the crown from Box 3 to Box 0
    (3, 0, 'newspaper'),       # Move the newspaper from Box 3 to Box 0
    (3, 0, 'television'),      # Move the television from Box 3 to Box 0
    (None, 6, 'sheet')         # Put the sheet into Box 6
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