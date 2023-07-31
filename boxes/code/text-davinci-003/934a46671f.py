# Initialize the boxes
boxes = {
    0: ['shell'],
    1: ['book', 'magazine', 'rose'],
    2: ['knife', 'tape'],
    3: ['fig', 'mirror'],
    4: [],
    5: ['dress'],
    6: ['drug', 'jacket'],
}

# Define the moves
moves = [
    (0, None, 'shell'),         # Remove the shell from Box 0
    (1, 4, 'book'),             # Move the book from Box 1 to Box 4
    (1, 4, 'magazine'),         # Move the magazine from Box 1 to Box 4
    (1, 4, 'rose'),             # Move the rose from Box 1 to Box 4
    (6, 1, 'jacket'),           # Move the jacket from Box 6 to Box 1
    (4, None, 'rose'),          # Remove the rose from Box 4
    (5, 2, 'dress'),            # Move the dress from Box 5 to Box 2
    (None, 5, 'card'),          # Put the card into Box 5
    (None, 5, 'string'),        # Put the string into Box 5
    (1, 0, 'jacket'),           # Move the jacket from Box 1 to Box 0
    (0, 4, 'jacket'),           # Move the jacket from Box 0 to Box 4
    (None, 0, 'cake'),          # Put the cake into Box 0
    (4, None, 'book'),          # Remove the book from Box 4
    (4, None, 'jacket'),        # Remove the jacket from Box 4
    (4, None, 'magazine'),      # Remove the magazine from Box 4
    (None, 6, 'ball')           # Put the ball into Box 6
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