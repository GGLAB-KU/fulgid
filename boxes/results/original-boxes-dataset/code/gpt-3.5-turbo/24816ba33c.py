# Initialize the boxes
boxes = {
    0: ['bag', 'radio'],
    1: ['meat'],
    2: ['shoe'],
    3: [],
    4: ['fish', 'wire'],
    5: ['plant'],
    6: ['painting', 'wheel'],
}

# Define the moves
moves = [
    (None, 5, 'glass'),       # Put the glass into Box 5
    (5, None, 'plant'),       # Remove the plant from Box 5
    (1, 5, 'meat'),           # Move the meat from Box 1 to Box 5
    (4, 2, 'fish'),           # Move the fish from Box 4 to Box 2
    (2, None, 'shoe'),        # Remove the shoe from Box 2
    (None, 1, 'cigarette'),   # Put the cigarette into Box 1
    (5, None, 'glass'),       # Remove the glass from Box 5
    (5, None, 'meat'),        # Remove the meat from Box 5
    (4, None, 'wire'),        # Remove the wire from Box 4
    (2, 5, 'fish'),           # Move the fish from Box 2 to Box 5
    (0, None, 'radio'),       # Remove the radio from Box 0
    (0, None, 'bag')          # Remove the bag from Box 0
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