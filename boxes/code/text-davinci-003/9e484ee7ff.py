# Initialize the boxes
boxes = {
    0: ['picture', 'tea'],
    1: ['bag', 'card'],
    2: ['seed', 'wheel'],
    3: ['boat', 'ice', 'jacket'],
    4: ['bread', 'computer', 'document'],
    5: ['game'],
    6: ['dish', 'meat', 'shoe'],
}

# Define the moves
moves = [
    (None, 0, 'pot'),       # Put the pot into Box 0
    (0, None, 'picture'),   # Remove the picture from Box 0
    (0, None, 'pot'),       # Remove the pot from Box 0
    (0, None, 'tea'),       # Remove the tea from Box 0
    (5, 2, 'game'),         # Move the game from Box 5 to Box 2
    (1, None, 'card'),      # Remove the card from Box 1
    (1, None, 'bag'),       # Remove the bag from Box 1
    (6, 0, 'shoe'),         # Move the shoe from Box 6 to Box 0
    (None, 6, 'bus'),       # Put the bus into Box 6
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