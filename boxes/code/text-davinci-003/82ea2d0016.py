# Initialize the boxes
boxes = {
    0: ['cross', 'egg'],
    1: ['bomb', 'card'],
    2: [],
    3: [],
    4: ['branch', 'stone'],
    5: ['clock', 'tie'],
    6: ['creature'],
}

# Define the moves
moves = [
    (6, None, 'creature'),   # Remove the creature from Box 6
    (None, 1, 'coffee'),     # Put the coffee into Box 1
    (0, 3, 'egg'),           # Move the egg from Box 0 to Box 3
    (None, 4, 'wire'),       # Put the wire into Box 4
    (None, 3, 'seed'),       # Put the seed into Box 3
    (0, 3, 'cross'),         # Move the cross from Box 0 to Box 3
    (4, None, 'branch'),     # Remove the branch from Box 4
    (4, None, 'stone'),      # Remove the stone from Box 4
    (4, None, 'wire'),       # Remove the wire from Box 4
    (None, 2, 'beer'),       # Put the beer into Box 2
    (3, None, 'cross'),      # Remove the cross from Box 3
    (3, None, 'egg'),        # Remove the egg from Box 3
    (3, None, 'seed'),       # Remove the seed from Box 3
    (5, 3, 'tie'),           # Move the tie from Box 5 to Box 3
    (1, 0, 'bomb'),          # Move the bomb from Box 1 to Box 0
    (1, 0, 'coffee')         # Move the coffee from Box 1 to Box 0
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