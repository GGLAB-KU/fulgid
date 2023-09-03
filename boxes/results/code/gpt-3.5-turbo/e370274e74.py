# Initialize the boxes
boxes = {
    0: ['mirror', 'sheet', 'tape'],
    1: ['boat', 'wheel'],
    2: ['card', 'television'],
    3: ['cheese', 'map', 'picture'],
    4: ['file', 'machine'],
    5: ['glass', 'watch'],
    6: ['block'],
}

# Define the moves
moves = [
    (5, 4, 'watch'),        # Move the watch from Box 5 to Box 4
    (5, None, 'glass'),     # Remove the glass from Box 5
    (3, 5, 'picture'),      # Move the picture from Box 3 to Box 5
    (0, None, 'mirror'),    # Remove the mirror from Box 0
    (0, None, 'sheet'),     # Remove the sheet from Box 0
    (0, None, 'tape'),      # Remove the tape from Box 0
    (None, 2, 'key'),       # Put the key into Box 2
    (1, None, 'boat'),      # Remove the boat from Box 1
    (2, None, 'television'), # Remove the television from Box 2
    (2, None, 'card'),      # Remove the card from Box 2
    (6, 2, 'block'),        # Move the block from Box 6 to Box 2
    (2, 3, 'block'),        # Move the block from Box 2 to Box 3
    (4, 6, 'machine'),      # Move the machine from Box 4 to Box 6
    (4, 6, 'watch'),        # Move the watch from Box 4 to Box 6
    (3, None, 'block'),     # Remove the block from Box 3
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