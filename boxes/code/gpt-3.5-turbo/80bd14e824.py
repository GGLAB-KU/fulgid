# Initialize the boxes
boxes = {
    0: [],
    1: ['cigarette', 'suit'],
    2: [],
    3: ['crown'],
    4: ['chemical', 'fan'],
    5: ['seed', 'tie'],
    6: ['bottle', 'drink', 'jacket'],
}

# Define the moves
moves = [
    (5, None, 'seed'),       # Remove the seed from Box 5
    (3, None, 'crown'),      # Remove the crown from Box 3
    (6, None, 'bottle'),     # Remove the bottle from Box 6
    (6, None, 'jacket'),     # Remove the jacket from Box 6
    (None, 3, 'book'),       # Put the book into Box 3
    (4, None, 'chemical'),   # Remove the chemical from Box 4
    (4, None, 'fan'),        # Remove the fan from Box 4
    (None, 5, 'bus'),        # Put the bus into Box 5
    (1, None, 'suit'),       # Remove the suit from Box 1
    (1, 4, 'cigarette'),     # Move the cigarette from Box 1 to Box 4
    (None, 1, 'leaf')        # Put the leaf into Box 1
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