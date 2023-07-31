# Initialize the boxes
boxes = {
    0: [],
    1: ['leaf', 'pipe'],
    2: ['chemical', 'map', 'wire'],
    3: ['cash'],
    4: ['newspaper'],
    5: ['book', 'tie'],
    6: ['watch'],
}

# Define the moves
moves = [
    (4, None, 'newspaper'),   # Remove the newspaper from Box 4
    (3, 1, 'cash'),           # Move the cash from Box 3 to Box 1
    (None, 4, 'block'),       # Put the block into Box 4
    (None, 3, 'boot'),        # Put the boot into Box 3
    (1, 4, 'leaf'),           # Move the leaf from Box 1 to Box 4
    (1, 4, 'pipe'),           # Move the pipe from Box 1 to Box 4
    (3, 6, 'boot'),           # Move the boot from Box 3 to Box 6
    (4, None, 'leaf'),        # Remove the leaf from Box 4
    (None, 0, 'sheet'),       # Put the sheet into Box 0
    (None, 0, 'rose'),        # Put the rose into Box 0
    (None, 4, 'engine'),      # Put the engine into Box 4
    (None, 3, 'glass'),       # Put the glass into Box 3
    (None, 3, 'meat')         # Put the meat into Box 3
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