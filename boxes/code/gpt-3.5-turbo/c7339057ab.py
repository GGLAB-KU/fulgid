# Initialize the boxes
boxes = {
    0: ['plant'],
    1: ['bomb', 'bowl'],
    2: ['drink', 'seed'],
    3: ['bone', 'coffee', 'painting'],
    4: ['clock', 'leaf'],
    5: ['radio', 'shoe', 'stone'],
    6: [],
}

# Define the moves
moves = [
    (None, 6, 'machine'),   # Put the machine into Box 6
    (5, None, 'painting'),   # Remove the painting from Box 5
    (5, None, 'fish'),       # Remove the fish from Box 5
    (3, 4, 'machine'),       # Move the machine from Box 3 to Box 4
    (3, 4, 'rose'),          # Move the rose from Box 3 to Box 4
    (6, 1, 'cross'),         # Move the cross from Box 6 to Box 1
    (1, 3, 'cross'),         # Move the cross from Box 1 to Box 3
    (3, 6, 'cross'),         # Move the cross from Box 3 to Box 6
    (6, 0, 'cross'),         # Move the cross from Box 6 to Box 0
    (None, 3, 'bell'),       # Put the bell into Box 3
    (None, 3, 'bottle')      # Put the bottle into Box 3
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