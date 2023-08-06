# Initialize the boxes
boxes = {
    0: ['chemical'],
    1: ['ball', 'tie'],
    2: ['bread'],
    3: ['plane'],
    4: [],
    5: ['boot'],
    6: ['card', 'clock', 'plate'],
}

# Define the moves
moves = [
    (1, None, 'ball'),       # Remove the ball from Box 1
    (6, None, 'card'),       # Remove the card from Box 6
    (6, None, 'clock'),      # Remove the clock from Box 6
    (6, None, 'plate'),      # Remove the plate from Box 6
    (5, 6, 'boot'),          # Move the boot from Box 5 to Box 6
    (3, None, 'plane'),      # Remove the plane from Box 3
    (0, 5, 'chemical'),      # Move the chemical from Box 0 to Box 5
    (2, 6, 'bread'),         # Move the bread from Box 2 to Box 6
    (1, None, 'tie'),        # Remove the tie from Box 1
    (None, 1, 'creature'),   # Put the creature into Box 1
    (None, 1, 'ice'),        # Put the ice into Box 1
    (5, 4, 'chemical'),      # Move the chemical from Box 5 to Box 4
    (None, 5, 'note'),       # Put the note into Box 5
    (None, 5, 'tissue'),     # Put the tissue into Box 5
    (None, 5, 'television'),  # Put the television into Box 5
    (6, None, 'boot'),       # Remove the boot from Box 6
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