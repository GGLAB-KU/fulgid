# Initialize the boxes
boxes = {
    0: ['book', 'game', 'tea'],
    1: ['drug', 'note', 'ring'],
    2: [],
    3: ['string'],
    4: ['tissue'],
    5: ['bell'],
    6: ['television'],
}

# Define the moves
moves = [
    (1, 2, 'drug'),     # Move the drug from Box 1 to Box 2
    (1, 2, 'ring'),     # Move the ring from Box 1 to Box 2
    (3, None, 'string'),    # Remove the string from Box 3
    (5, None, 'bell'),      # Remove the bell from Box 5
    (None, 5, 'milk'),      # Put the milk into Box 5
    (6, None, 'television'),    # Remove the television from Box 6
    (4, None, 'tissue'),    # Remove the tissue from Box 4
    (0, 4, 'game'),     # Move the game from Box 0 to Box 4
    (None, 2, 'shell')      # Put the shell into Box 2
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