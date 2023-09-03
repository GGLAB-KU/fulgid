# Initialize the boxes
boxes = {
    0: [],
    1: ['document', 'drug', 'medicine'],
    2: ['apple', 'drink', 'jacket'],
    3: [],
    4: ['bowl', 'camera', 'shirt'],
    5: ['boot', 'dish', 'file'],
    6: ['branch', 'map', 'wire'],
}

# Define the moves
moves = [
    (2, None, 'apple'),     # Remove the apple from Box 2
    (2, None, 'drink'),     # Remove the drink from Box 2
    (1, None, 'document'),  # Remove the document from Box 1
    (1, None, 'drug'),      # Remove the drug from Box 1
    (5, None, 'file'),      # Remove the file from Box 5
    (5, None, 'boot'),      # Remove the boot from Box 5
    (5, None, 'dish'),      # Remove the dish from Box 5
    (4, 3, 'bowl'),         # Move the bowl from Box 4 to Box 3
    (4, 3, 'shirt'),        # Move the shirt from Box 4 to Box 3
    (3, None, 'bowl'),      # Remove the bowl from Box 3
    (3, None, 'shirt'),     # Remove the shirt from Box 3
    (6, None, 'branch'),    # Remove the branch from Box 6
    (6, None, 'map'),       # Remove the map from Box 6
    (6, None, 'wire'),      # Remove the wire from Box 6
    (2, None, 'jacket'),    # Remove the jacket from Box 2
    (None, 5, 'rock')       # Put the rock into Box 5
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