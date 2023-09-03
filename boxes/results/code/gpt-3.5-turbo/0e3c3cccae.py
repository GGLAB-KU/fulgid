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