# Initialize the boxes
boxes = {
    0: [],
    1: ['fan', 'fig', 'tissue'],
    2: ['seed'],
    3: ['cross'],
    4: [],
    5: ['card', 'disk'],
    6: [],
}

# Define the moves
moves = [
    (1, 0, 'fig'),         # Move the fig from Box 1 to Box 0
    (None, 4, 'coat'),     # Put the coat into Box 4
    (None, 0, 'cigarette'),# Put the cigarette into Box 0
    (4, None, 'coat'),     # Remove the coat from Box 4
    (2, 5, 'seed'),        # Move the seed from Box 2 to Box 5
    (3, None, 'cross'),    # Remove the cross from Box 3
    (5, None, 'disk'),     # Remove the disk from Box 5
    (5, None, 'seed'),     # Remove the seed from Box 5
    (0, 3, 'cigarette'),   # Move the cigarette from Box 0 to Box 3
    (5, None, 'card'),     # Remove the card from Box 5
    (None, 5, 'train'),    # Put the train into Box 5
    (0, 2, 'fig'),         # Move the fig from Box 0 to Box 2
    (1, 0, 'fan'),         # Move the fan from Box 1 to Box 0
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