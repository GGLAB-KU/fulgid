# Initialize the boxes
boxes = {
    0: ['seed'],
    1: ['dress'],
    2: ['picture'],
    3: ['bowl', 'computer'],
    4: ['bomb', 'tea'],
    5: [],
    6: ['cigarette'],
}

# Define the moves
moves = [
    (1, 5, 'dress'),        # Move the dress from Box 1 to Box 5
    (None, 4, 'stone'),     # Put the stone into Box 4
    (2, None, 'picture'),   # Remove the picture from Box 2
    (5, None, 'dress'),     # Remove the dress from Box 5
    (None, 1, 'radio'),     # Put the radio into Box 1
    (1, None, 'radio'),     # Remove the radio from Box 1
    (0, None, 'seed'),      # Remove the seed from Box 0
    (None, 5, 'drink'),     # Put the drink into Box 5
    (4, 6, 'stone'),        # Move the stone from Box 4 to Box 6
    (4, 6, 'tea'),          # Move the tea from Box 4 to Box 6
    (None, 3, 'coat'),      # Put the coat into Box 3
    (0, 4, 'seed')          # Put the seed into Box 4
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