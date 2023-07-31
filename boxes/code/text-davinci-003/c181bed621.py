# Initialize the boxes
boxes = {
    0: ['fan', 'tape'],
    1: ['shell'],
    2: [],
    3: ['bomb', 'radio'],
    4: ['fish', 'ring'],
    5: ['computer'],
    6: ['plane'],
}

# Define the moves
moves = [
    (4, 5, 'fish'),         # Move the fish from Box 4 to Box 5
    (4, None, 'fish'),      # Remove the fish from Box 4
    (6, None, 'plane'),     # Remove the plane from Box 6
    (3, None, 'radio'),     # Remove the radio from Box 3
    (0, 6, 'fan'),          # Move the fan from Box 0 to Box 6
    (0, 6, 'tape'),         # Move the tape from Box 0 to Box 6
    (6, None, 'fan'),       # Remove the fan from Box 6
    (None, 4, 'shirt'),     # Put the shirt into Box 4
    (None, 4, 'tea'),       # Put the tea into Box 4
    (None, 3, 'shoe'),      # Put the shoe into Box 3
    (4, 5, 'tea')           # Move the tea from Box 4 to Box 5
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