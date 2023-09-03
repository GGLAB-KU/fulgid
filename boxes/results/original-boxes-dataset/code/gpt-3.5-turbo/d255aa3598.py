# Initialize the boxes
boxes = {
    0: ['cigarette'],
    1: ['document'],
    2: ['shirt'],
    3: ['cream', 'drink', 'plant'],
    4: ['branch', 'ice'],
    5: ['watch'],
    6: ['car', 'machine', 'meat'],
}

# Define the moves
moves = [
    (0, None, 'cigarette'),     # Remove the cigarette from Box 0
    (3, None, 'cream'),         # Remove the cream from Box 3
    (3, None, 'plant'),         # Remove the plant from Box 3
    (1, None, 'document'),      # Remove the document from Box 1
    (None, 1, 'chemical'),       # Put the chemical into Box 1
    (1, None, 'chemical'),       # Remove the chemical from Box 1
    (5, None, 'watch'),         # Remove the watch from Box 5
    (4, None, 'ice'),           # Remove the ice from Box 4
    (6, 2, 'meat'),             # Move the meat from Box 6 to Box 2
    (2, 1, 'meat'),             # Move the meat from Box 2 to Box 1
    (2, 1, 'shirt'),            # Move the shirt from Box 2 to Box 1
    (None, 5, 'bill'),          # Put the bill into Box 5
    (1, None, 'meat')           # Remove the meat from Box 1
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