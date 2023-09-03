# Initialize the boxes
boxes = {
    0: ['card', 'leaf'],
    1: [],
    2: ['apple', 'picture'],
    3: ['bag', 'hat', 'wheel'],
    4: ['bottle', 'drink', 'tape'],
    5: ['brick', 'plant', 'wire'],
    6: ['rose'],
}

# Define the moves
moves = [
    (3, 6, 'bag'),         # Move the bag from Box 3 to Box 6
    (3, 6, 'hat'),         # Move the hat from Box 3 to Box 6
    (5, None, 'brick'),    # Remove the brick from Box 5
    (6, 1, 'hat'),         # Move the hat from Box 6 to Box 1
    (1, 3, 'hat'),         # Move the hat from Box 1 to Box 3
    (2, None, 'picture'),  # Remove the picture from Box 2
    (None, 5, 'milk'),     # Put the milk into Box 5
    (None, 3, 'egg'),      # Put the egg into Box 3
    (0, None, 'leaf'),     # Remove the leaf from Box 0
    (5, 2, 'plant'),       # Move the plant from Box 5 to Box 2
    (5, 2, 'wire'),        # Move the wire from Box 5 to Box 2
    (5, 1, 'milk'),        # Move the milk from Box 5 to Box 1
    (4, None, 'bottle'),   # Remove the bottle from Box 4
    (4, None, 'tape')      # Remove the tape from Box 4
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