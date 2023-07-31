# Initialize the boxes
boxes = {
    0: ['ball', 'shoe'],
    1: ['stone'],
    2: ['sheet', 'wire'],
    3: ['book', 'boot', 'shirt'],
    4: ['branch'],
    5: ['creature'],
    6: ['beer', 'bell', 'coffee'],
}

# Define the moves
moves = [
    (1, 5, 'stone'),        # Move the stone from Box 1 to Box 5
    (2, 0, 'wire'),         # Move the wire from Box 2 to Box 0
    (2, None, 'sheet'),     # Remove the sheet from Box 2
    (None, 1, 'letter'),    # Put the letter into Box 1
    (6, None, 'beer'),      # Remove the beer from Box 6
    (6, None, 'bell'),      # Remove the bell from Box 6
    (6, None, 'coffee'),    # Remove the coffee from Box 6
    (None, 4, 'fig'),       # Put the fig into Box 4
    (None, 4, 'ring'),      # Put the ring into Box 4
    (5, 6, 'stone'),        # Move the stone from Box 5 to Box 6
    (5, None, 'creature'),  # Remove the creature from Box 5
    (6, None, 'stone'),     # Remove the stone from Box 6
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