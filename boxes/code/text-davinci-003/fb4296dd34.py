# Initialize the boxes
boxes = {
    0: [],
    1: ['egg', 'medicine', 'wheel'],
    2: ['file', 'tie'],
    3: [],
    4: ['boot', 'suit'],
    5: ['fig', 'seed'],
    6: ['beer', 'meat'],
}

# Define the moves
moves = [
    (2, 5, 'file'),         # Move the file from Box 2 to Box 5
    (6, None, 'beer'),      # Remove the beer from Box 6
    (None, 4, 'watch'),     # Put the watch into Box 4
    (None, 3, 'drug'),      # Put the drug into Box 3
    (None, 3, 'guitar'),    # Put the guitar into Box 3
    (1, 6, 'egg'),          # Move the egg from Box 1 to Box 6
    (1, 6, 'wheel'),        # Move the wheel from Box 1 to Box 6
    (None, 2, 'brick'),     # Put the brick into Box 2
    (None, 2, 'coffee'),    # Put the coffee into Box 2
    (1, None, 'medicine'),  # Remove the medicine from Box 1
    (2, None, 'coffee'),    # Remove the coffee from Box 2
    (2, None, 'tie'),       # Remove the tie from Box 2
    (4, None, 'suit'),      # Remove the suit from Box 4
    (4, None, 'watch'),     # Remove the watch from Box 4
    (4, None, 'boot'),      # Remove the boot from Box 4
    (6, 2, 'egg'),          # Move the egg from Box 6 to Box 2
    (6, 2, 'meat'),         # Move the meat from Box 6 to Box 2
    (6, None, 'wheel'),     # Remove the wheel from Box 6
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