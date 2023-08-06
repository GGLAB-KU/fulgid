# Initialize the boxes
boxes = {
    0: ['watch'],
    1: ['brain', 'drink', 'sheet'],
    2: ['ball', 'cup', 'tie'],
    3: ['key', 'rock', 'shell'],
    4: ['computer', 'disk', 'note'],
    5: ['bomb', 'fish', 'guitar'],
    6: ['coffee', 'cross', 'tissue'],
}

# Define the moves
moves = [
    (None, 0, 'bread'),        # Put the bread into Box 0
    (None, 0, 'creature'),     # Put the creature into Box 0
    (1, None, 'drink'),        # Remove the drink from Box 1
    (1, None, 'sheet'),        # Remove the sheet from Box 1
    (5, None, 'bomb'),         # Remove the bomb from Box 5
    (0, None, 'creature'),     # Remove the creature from Box 0
    (2, None, 'ball'),         # Remove the ball from Box 2
    (2, None, 'cup'),          # Remove the cup from Box 2
    (2, None, 'tie'),          # Remove the tie from Box 2
    (6, 1, 'tissue'),          # Move the tissue from Box 6 to Box 1
    (3, 6, 'shell'),           # Move the shell from Box 3 to Box 6
    (5, None, 'guitar'),       # Remove the guitar from Box 5
    (5, None, 'fish'),         # Remove the fish from Box 5
    (0, None, 'bread'),        # Remove the bread from Box 0
    (0, None, 'watch'),        # Remove the watch from Box 0
    (None, 3, 'bomb'),         # Put the bomb into Box 3
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