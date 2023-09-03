# Initialize the boxes
boxes = {
    0: ['beer', 'coffee', 'wheel'],
    1: ['cake', 'rock', 'tissue'],
    2: ['boot', 'drug', 'leaf'],
    3: ['magazine'],
    4: ['brick', 'cigarette'],
    5: ['shoe'],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'boot'),       # Remove the boot from Box 2
    (None, 4, 'pot'),        # Put the pot into Box 4
    (0, 5, 'coffee'),        # Move the coffee from Box 0 to Box 5
    (0, 2, 'wheel'),         # Move the wheel from Box 0 to Box 2
    (0, None, 'beer'),       # Remove the beer from Box 0
    (1, 5, 'rock'),          # Move the rock from Box 1 to Box 5
    (1, None, 'tissue'),     # Remove the tissue from Box 1
    (4, 1, 'brick'),         # Move the brick from Box 4 to Box 1
    (2, 0, 'wheel'),         # Move the wheel from Box 2 to Box 0
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