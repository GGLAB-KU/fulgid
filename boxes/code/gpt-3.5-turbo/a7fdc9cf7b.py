# Initialize the boxes
boxes = {
    0: ['letter'],
    1: [],
    2: ['bell', 'dress'],
    3: ['chemical', 'sheet', 'string'],
    4: ['crown', 'plane', 'tape'],
    5: ['beer'],
    6: [],
}

# Define the moves
moves = [
    (None, 6, 'bus'),       # Put the bus into Box 6
    (None, 6, 'train'),     # Put the train into Box 6
    (None, 6, 'cream'),     # Put the cream into Box 6
    (3, None, 'chemical'),  # Remove the chemical from Box 3
    (5, 0, 'beer'),         # Move the beer from Box 5 to Box 0
    (3, None, 'sheet'),     # Remove the sheet from Box 3
    (None, 3, 'bill'),      # Put the bill into Box 3
    (None, 3, 'shirt'),     # Put the shirt into Box 3
    (6, None, 'bus'),       # Remove the bus from Box 6
    (None, 6, 'mirror'),    # Put the mirror into Box 6
    (2, None, 'apple'),     # Put the apple into Box 2
    (2, 1, 'dress'),        # Move the dress from Box 2 to Box 1
    (1, 0, 'dress'),        # Move the dress from Box 1 to Box 0
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