# Initialize the boxes
boxes = {
    0: ['magazine', 'phone', 'watch'],
    1: [],
    2: ['chemical'],
    3: ['cross'],
    4: [],
    5: ['machine', 'train'],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'chemical'),     # Remove the chemical from Box 2
    (5, None, 'train'),        # Remove the train from Box 5
    (None, 6, 'document'),     # Put the document into Box 6
    (5, 3, 'machine'),         # Move the machine from Box 5 to Box 3
    (0, 4, 'magazine'),        # Move the magazine from Box 0 to Box 4
    (0, 4, 'watch'),           # Move the watch from Box 0 to Box 4
    (3, None, 'cross'),        # Remove the cross from Box 3
    (3, None, 'machine'),      # Remove the machine from Box 3
    (6, None, 'document'),     # Remove the document from Box 6
    (0, 5, 'phone')            # Move the phone from Box 0 to Box 5
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