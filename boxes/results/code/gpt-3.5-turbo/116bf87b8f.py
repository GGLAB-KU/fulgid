# Initialize the boxes
boxes = {
    0: ['coat'],
    1: ['bomb', 'train'],
    2: ['book', 'magazine'],
    3: ['chemical'],
    4: ['cake', 'phone', 'seed'],
    5: ['cross', 'hat', 'mirror'],
    6: ['fish', 'glass'],
}

# Define the moves
moves = [
    (1, None, 'train'),     # Remove the train from Box 1
    (6, 2, 'glass'),        # Move the glass from Box 6 to Box 2
    (0, None, 'coat'),      # Remove the coat from Box 0
    (None, 6, 'key'),       # Put the key into Box 6
    (4, None, 'phone'),     # Remove the phone from Box 4
    (None, 1, 'fig'),       # Put the fig into Box 1
    (None, 0, 'bread'),     # Put the bread into Box 0
    (None, 0, 'creature'),  # Put the creature into Box 0
    (5, None, 'hat'),       # Remove the hat from Box 5
    (6, None, 'fish'),      # Remove the fish from Box 6
    (6, None, 'key'),       # Remove the key from Box 6
    (5, None, 'cross'),     # Remove the cross from Box 5
    (5, None, 'mirror'),    # Remove the mirror from Box 5
    (1, 5, 'fig'),          # Move the fig from Box 1 to Box 5
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