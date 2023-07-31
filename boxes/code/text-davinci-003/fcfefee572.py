# Initialize the boxes
boxes = {
    0: [],
    1: ['book', 'brick', 'pipe'],
    2: [],
    3: ['rock'],
    4: ['shirt', 'tea', 'watch'],
    5: ['boat', 'bottle', 'ice'],
    6: ['ball', 'fan', 'file'],
}

# Define the moves
moves = [
    (5, None, 'boat'),       # Remove the boat from Box 5
    (5, None, 'boat'),       # Put the boat into Box 5
    (None, 3, 'coffee'),     # Put the coffee into Box 3
    (None, 3, 'ticket'),     # Put the ticket into Box 3
    (4, None, 'tea'),        # Remove the tea from Box 4
    (1, 2, 'pipe'),          # Move the pipe from Box 1 to Box 2
    (None, 4, 'television'),  # Put the television into Box 4
    (None, 2, 'document'),   # Put the document into Box 2
    (3, None, 'coffee'),     # Remove the coffee from Box 3
    (3, None, 'ticket'),     # Remove the ticket from Box 3
    (1, None, 'book'),       # Remove the book from Box 1
    (1, None, 'brick'),      # Remove the brick from Box 1
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