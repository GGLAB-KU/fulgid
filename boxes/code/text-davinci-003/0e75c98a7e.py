# Initialize the boxes
boxes = {
    0: ['bus', 'leaf', 'ring'],
    1: [],
    2: ['key', 'tie'],
    3: ['cake', 'chemical', 'watch'],
    4: ['coat', 'paper', 'tissue'],
    5: ['string', 'ticket'],
    6: ['cheese', 'cigarette'],
}

# Define the moves
moves = [
    (5, 2, 'ticket'),   # Move the ticket from Box 5 to Box 2
    (0, None, 'leaf')   # Remove the leaf from Box 0
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