# Initialize the boxes
boxes = {
    0: ['dress', 'key'],
    1: [],
    2: ['mirror', 'tape', 'train'],
    3: ['block', 'car'],
    4: ['fig', 'watch'],
    5: ['bread', 'rock'],
    6: ['bag', 'note', 'rose'],
}

# Define the moves
moves = [
    (4, None, 'watch'),       # Remove the watch from Box 4
    (4, 1, 'fig'),            # Move the fig from Box 4 to Box 1
    (None, 0, 'computer'),    # Put the computer into Box 0
    (6, None, 'rose'),        # Remove the rose from Box 6
    (3, None, 'car'),         # Remove the car from Box 3
    (None, 4, 'hat'),         # Put the hat into Box 4
    (2, None, 'mirror'),      # Remove the mirror from Box 2
    (2, None, 'train'),       # Remove the train from Box 2
    (1, 2, 'fig'),            # Move the fig from Box 1 to Box 2
    (4, 2, 'hat'),            # Move the hat from Box 4 to Box 2
    (2, 4, 'fig'),            # Move the fig from Box 2 to Box 4
    (2, 4, 'hat'),            # Move the hat from Box 2 to Box 4
    (2, 4, 'tape'),           # Move the tape from Box 2 to Box 4
    (None, 2, 'wire'),        # Put the wire into Box 2
    (2, 1, 'wire'),           # Move the wire from Box 2 to Box 1
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