# Initialize the boxes
boxes = {
    0: ['card', 'cash'],
    1: ['bone', 'boot', 'pot'],
    2: ['bill', 'seed'],
    3: ['paper'],
    4: ['fish'],
    5: ['brain', 'file'],
    6: ['ball', 'boat', 'medicine'],
}

# Define the moves
moves = [
    (1, None, 'bone'),      # Remove the bone from Box 1
    (1, None, 'boot'),      # Remove the boot from Box 1
    (1, None, 'pot'),       # Remove the pot from Box 1
    (None, 1, 'bone'),      # Put the bone into Box 1
    (None, 1, 'mirror'),    # Put the mirror into Box 1
    (4, 0, 'fish'),         # Move the fish from Box 4 to Box 0
    (1, None, 'mirror'),    # Remove the mirror from Box 1
    (None, 5, 'tie'),       # Put the tie into Box 5
    (5, None, 'brain'),     # Remove the brain from Box 5
    (0, None, 'card'),      # Remove the card from Box 0
    (3, None, 'paper'),     # Remove the paper from Box 3
    (0, None, 'cash'),      # Remove the cash from Box 0
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