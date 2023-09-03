# Initialize the boxes
boxes = {
    0: [],
    1: ['television'],
    2: ['tea'],
    3: ['bread', 'coat'],
    4: [],
    5: ['plane'],
    6: ['disk'],
}

# Define the moves
moves = [
    (2, 4, 'tea'),       # Move the tea from Box 2 to Box 4
    (5, 1, 'plane'),     # Move the plane from Box 5 to Box 1
    (6, None, 'disk'),   # Remove the disk from Box 6
    (4, 2, 'tea'),       # Move the tea from Box 4 to Box 2
    (None, 6, 'tie'),    # Put the tie into Box 6
    (None, 6, 'tissue'), # Put the tissue into Box 6
    (2, None, 'tea'),    # Remove the tea from Box 2
    (None, 3, 'boat'),   # Put the boat into Box 3
    (None, 5, 'fig'),    # Put the fig into Box 5
    (None, 5, 'shell'),  # Put the shell into Box 5
    (None, 6, 'card')    # Put the card into Box 6
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