# Initialize the boxes
boxes = {
    0: ['pot'],
    1: ['flower'],
    2: [],
    3: ['game', 'watch'],
    4: ['cross', 'phone', 'tea'],
    5: ['cheese', 'ticket'],
    6: ['cake'],
}

# Define the moves
moves = [
    (None, 2, 'creature'),     # Put the creature into Box 2
    (0, 5, 'pot'),             # Move the pot from Box 0 to Box 5
    (5, 1, 'pot'),             # Move the pot from Box 5 to Box 1
    (6, None, 'cake'),         # Remove the cake from Box 6
    (4, 0, 'phone'),           # Move the phone from Box 4 to Box 0
    (4, 0, 'tea'),             # Move the tea from Box 4 to Box 0
    (5, 3, 'cheese'),          # Move the cheese from Box 5 to Box 3
    (5, 2, 'ticket'),          # Move the ticket from Box 5 to Box 2
    (3, None, 'game'),         # Remove the game from Box 3
    (3, None, 'watch'),        # Remove the watch from Box 3
    (0, 3, 'phone'),           # Move the phone from Box 0 to Box 3
    (None, 3, 'glass')         # Put the glass into Box 3
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