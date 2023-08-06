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
    (None, 3, 'book')        # Put the book into Box 3
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