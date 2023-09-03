# Initialize the boxes
boxes = {
    0: ['magazine'],
    1: ['plant'],
    2: ['apple', 'bell', 'crown'],
    3: [],
    4: ['pipe', 'plate', 'rock'],
    5: ['painting'],
    6: [],
}

# Define the moves
moves = [
    (None, 3, 'branch'),       # Put the branch into Box 3
    (None, 3, 'chemical'),     # Put the chemical into Box 3
    (None, 3, 'cigarette'),    # Put the cigarette into Box 3
    (None, 5, 'fan'),          # Put the fan into Box 5
    (5, None, 'fan'),          # Remove the fan from Box 5
    (5, None, 'painting'),     # Remove the painting from Box 5
    (2, None, 'apple'),        # Remove the apple from Box 2
    (3, None, 'chemical'),     # Remove the chemical from Box 3
    (3, None, 'cigarette'),    # Remove the cigarette from Box 3
    (None, 6, 'drink'),        # Put the drink into Box 6
    (None, 6, 'note'),         # Put the note into Box 6
    (None, 3, 'document'),     # Put the document into Box 3
    (None, 3, 'map'),          # Put the map into Box 3
    (2, 5, 'bell'),            # Move the bell from Box 2 to Box 5
    (2, 5, 'crown'),           # Move the crown from Box 2 to Box 5
    (0, 1, 'magazine'),        # Move the magazine from Box 0 to Box 1
    (1, 5, 'magazine'),        # Move the magazine from Box 1 to Box 5
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