# Initialize the boxes
boxes = {
    0: ['computer', 'cream', 'glass'],
    1: [],
    2: ['flower', 'rose'],
    3: ['card', 'egg', 'plate'],
    4: ['brick', 'seed'],
    5: ['document', 'pipe'],
    6: ['dress', 'guitar'],
}

# Define the moves
moves = [
    (2, 1, 'rose'),         # Move the rose from Box 2 to Box 1
    (1, 2, 'rose'),         # Move the rose from Box 1 to Box 2
    (4, 1, 'brick'),        # Move the brick from Box 4 to Box 1
    (4, 1, 'seed'),         # Move the seed from Box 4 to Box 1
    (0, 2, 'cream'),        # Move the cream from Box 0 to Box 2
    (3, None, 'card'),      # Remove the card from Box 3
    (3, None, 'egg'),       # Remove the egg from Box 3
    (3, None, 'plate'),     # Remove the plate from Box 3
    (1, None, 'brick'),     # Remove the brick from Box 1
    (0, 4, 'computer'),     # Move the computer from Box 0 to Box 4
    (0, 4, 'glass'),        # Move the glass from Box 0 to Box 4
    (None, 4, 'knife'),     # Put the knife into Box 4
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