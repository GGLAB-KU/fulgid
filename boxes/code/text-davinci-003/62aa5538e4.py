# Initialize the boxes
boxes = {
    0: ['tea'],
    1: [],
    2: ['block', 'brain'],
    3: ['book', 'ice', 'ring'],
    4: ['creature', 'hat', 'wheel'],
    5: ['fig', 'note', 'train'],
    6: ['ball'],
}

# Define the moves
moves = [
    (2, 1, 'block'),        # Move the block from Box 2 to Box 1
    (None, 0, 'magazine'),  # Put the magazine into Box 0
    (None, 0, 'shirt'),     # Put the shirt into Box 0
    (4, 2, 'wheel'),        # Move the wheel from Box 4 to Box 2
    (5, None, 'train'),     # Remove the train from Box 5
    (None, 1, 'dress'),     # Put the dress into Box 1
    (4, None, 'creature'),  # Remove the creature from Box 4
    (3, None, 'book'),      # Remove the book from Box 3
    (3, None, 'ring')       # Remove the ring from Box 3
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