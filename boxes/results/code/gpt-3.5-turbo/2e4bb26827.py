# Initialize the boxes
boxes = {
    0: ['fig'],
    1: ['cream', 'paper'],
    2: ['bag', 'file'],
    3: ['car', 'ring', 'ticket'],
    4: ['fish', 'pot'],
    5: ['coat', 'coffee'],
    6: ['boot', 'knife'],
}

# Define the moves
moves = [
    (None, 0, 'egg'),       # Put the egg into Box 0
    (0, None, 'fig'),       # Remove the fig from Box 0
    (5, 6, 'coat'),         # Move the coat from Box 5 to Box 6
    (5, 0, 'coffee'),       # Move the coffee from Box 5 to Box 0
    (1, None, 'paper'),     # Remove the paper from Box 1
    (None, 1, 'bottle'),    # Put the bottle into Box 1
    (None, 1, 'jacket'),    # Put the jacket into Box 1
    (1, None, 'cream'),     # Remove the cream from Box 1
    (6, 1, 'coat'),         # Move the coat from Box 6 to Box 1
    (2, 4, 'bag'),          # Move the bag from Box 2 to Box 4
    (3, None, 'car'),       # Remove the car from Box 3
    (3, None, 'ring'),      # Remove the ring from Box 3
    (3, None, 'ticket'),    # Remove the ticket from Box 3
    (4, None, 'bag'),       # Remove the bag from Box 4
    (None, 3, 'creature'),  # Put the creature into Box 3
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