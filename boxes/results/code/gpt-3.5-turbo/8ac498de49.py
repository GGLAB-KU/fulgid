# Initialize the boxes
boxes = {
    0: ['branch', 'phone', 'shoe'],
    1: ['egg', 'game', 'pot'],
    2: ['pipe'],
    3: ['machine', 'train'],
    4: ['hat'],
    5: ['chemical'],
    6: ['bottle', 'coat', 'document'],
}

# Define the moves
moves = [
    (6, None, 'document'),      # Remove the document from Box 6
    (6, 5, 'bottle'),            # Move the bottle from Box 6 to Box 5
    (3, None, 'machine'),        # Remove the machine from Box 3
    (3, None, 'train'),          # Remove the train from Box 3
    (2, None, 'pipe'),           # Remove the pipe from Box 2
    (None, 2, 'television'),      # Put the television into Box 2
    (1, None, 'pot'),            # Remove the pot from Box 1
    (None, 2, 'book'),            # Put the book into Box 2
    (None, 2, 'plant'),           # Put the plant into Box 2
    (6, 1, 'coat'),              # Move the coat from Box 6 to Box 1
    (1, 3, 'coat'),              # Move the coat from Box 1 to Box 3
    (1, 3, 'egg'),               # Move the egg from Box 1 to Box 3
    (1, 3, 'game'),              # Move the game from Box 1 to Box 3
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