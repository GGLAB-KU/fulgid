# Initialize the boxes
boxes = {
    0: ['bell', 'document'],
    1: ['cross', 'medicine', 'radio'],
    2: ['beer', 'machine'],
    3: ['wire'],
    4: ['string'],
    5: ['apple', 'bottle'],
    6: ['bomb', 'pot', 'tape'],
}

# Define the moves
moves = [
    (0, None, 'bell'),       # Remove the bell from Box 0
    (0, None, 'document'),   # Remove the document from Box 0
    (3, None, 'wire'),       # Remove the wire from Box 3
    (None, 0, 'dress'),      # Put the dress into Box 0
    (5, 3, 'apple'),         # Move the apple from Box 5 to Box 3
    (5, 3, 'bottle'),        # Move the bottle from Box 5 to Box 3
    (2, None, 'machine'),    # Remove the machine from Box 2
    (None, 2, 'shell'),      # Put the shell into Box 2
    (4, None, 'string'),     # Remove the string from Box 4
    (3, 4, 'apple'),         # Move the apple from Box 3 to Box 4
    (2, None, 'shell'),      # Remove the shell from Box 2
    (None, 5, 'cream'),      # Put the cream into Box 5
    (None, 5, 'drink'),      # Put the drink into Box 5
    (None, 5, 'flower'),     # Put the flower into Box 5
    (6, 2, 'bomb'),          # Move the bomb from Box 6 to Box 2
    (6, 2, 'tape')           # Move the tape from Box 6 to Box 2
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