# Initialize the boxes
boxes = {
    0: ['game', 'knife', 'map'],
    1: ['magazine', 'note', 'string'],
    2: [],
    3: ['seed'],
    4: ['egg'],
    5: ['apple', 'bomb', 'rock'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'seed'),       # Remove the seed from Box 3
    (1, 4, 'string'),        # Move the string from Box 1 to Box 4
    (4, 3, 'string'),        # Move the string from Box 4 to Box 3
    (None, 6, 'machine'),    # Put the machine into Box 6
    (3, 4, 'string'),        # Move the string from Box 3 to Box 4
    (4, None, 'egg'),        # Remove the egg from Box 4
    (1, None, 'note'),       # Remove the note from Box 1
    (0, 3, 'game'),          # Move the game from Box 0 to Box 3
    (None, 4, 'cigarette'),  # Put the cigarette into Box 4
    (None, 4, 'painting')    # Put the painting into Box 4
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