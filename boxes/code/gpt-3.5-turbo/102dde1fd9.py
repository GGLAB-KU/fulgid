# Initialize the boxes
boxes = {
    0: ['apple'],
    1: ['seed', 'watch'],
    2: ['magazine'],
    3: [],
    4: ['bag', 'cigarette', 'engine'],
    5: ['creature', 'fan', 'shirt'],
    6: ['brick', 'pipe'],
}

# Define the moves
moves = [
    (None, 3, 'egg'),       # Put the egg into Box 3
    (None, 3, 'plant'),     # Put the plant into Box 3
    (None, 3, 'rock'),      # Put the rock into Box 3
    (4, None, 'bag'),       # Remove the bag from Box 4
    (4, None, 'engine'),    # Remove the engine from Box 4
    (1, 0, 'watch'),        # Move the watch from Box 1 to Box 0
    (1, 4, 'seed'),         # Move the seed from Box 1 to Box 4
    (3, 1, 'plant'),        # Move the plant from Box 3 to Box 1
    (2, None, 'magazine'),  # Remove the magazine from Box 2
    (1, None, 'plant'),     # Remove the plant from Box 1
    (4, 2, 'seed'),         # Move the seed from Box 4 to Box 2
    (2, None, 'seed'),      # Remove the seed from Box 2
    (None, 0, 'bill'),      # Put the bill into Box 0
    (4, 3, 'cigarette'),    # Move the cigarette from Box 4 to Box 3
    (3, None, 'cigarette'), # Remove the cigarette from Box 3
    (3, None, 'egg')        # Remove the egg from Box 3
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