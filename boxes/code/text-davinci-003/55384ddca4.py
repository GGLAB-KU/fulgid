# Initialize the boxes
boxes = {
    0: ['card', 'clock', 'glass'],
    1: ['mirror'],
    2: ['ring'],
    3: ['cake', 'cheese'],
    4: ['cross', 'shoe', 'stone'],
    5: ['fig'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'cake'),       # Remove the cake from Box 3
    (3, None, 'cheese'),     # Remove the cheese from Box 3
    (2, 1, 'ring'),          # Move the ring from Box 2 to Box 1
    (1, None, 'mirror'),     # Remove the mirror from Box 1
    (1, None, 'ring'),       # Remove the ring from Box 1
    (4, None, 'shoe'),       # Remove the shoe from Box 4
    (4, None, 'stone'),      # Remove the stone from Box 4
    (None, 5, 'branch'),     # Put the branch into Box 5
    (None, 5, 'seed'),       # Put the seed into Box 5
    (5, 3, 'branch'),        # Move the branch from Box 5 to Box 3
    (5, 3, 'fig'),           # Move the fig from Box 5 to Box 3
    (5, 3, 'seed'),          # Move the seed from Box 5 to Box 3
    (None, 5, 'radio'),      # Put the radio into Box 5
    (4, 5, 'cross'),         # Move the cross from Box 4 to Box 5
    (3, 2, 'seed'),          # Move the seed from Box 3 to Box 2
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