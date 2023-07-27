# Initialize the boxes
boxes = {
    0: ['bell', 'string'],
    1: ['bag', 'coat', 'machine'],
    2: ['jacket', 'letter', 'mirror'],
    3: [],
    4: ['cigarette', 'file', 'medicine'],
    5: ['shirt', 'television'],
    6: [],
}

# Define the moves
moves = [
    (4, 0, 'file'),         # Move the file from Box 4 to Box 0
    (0, None, 'file'),      # Remove the file from Box 0
    (None, 3, 'clock'),     # Put the clock into Box 3
    (None, 3, 'watch'),     # Put the watch into Box 3
    (2, None, 'jacket'),    # Remove the jacket from Box 2
    (2, None, 'mirror'),    # Remove the mirror from Box 2
    (3, 6, 'watch'),        # Move the watch from Box 3 to Box 6
    (0, None, 'bell'),      # Remove the bell from Box 0
    (2, 0, 'letter'),       # Move the letter from Box 2 to Box 0
    (None, 5, 'card'),      # Put the card into Box 5
    (5, 2, 'card'),         # Move the card from Box 5 to Box 2
    (5, 2, 'shirt'),        # Move the shirt from Box 5 to Box 2
    (5, 2, 'television'),   # Move the television from Box 5 to Box 2
    (0, None, 'letter'),    # Remove the letter from Box 0
    (2, 0, 'card'),         # Move the card from Box 2 to Box 0
    (2, 0, 'shirt'),        # Move the shirt from Box 2 to Box 0
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