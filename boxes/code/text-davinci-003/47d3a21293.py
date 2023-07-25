# Initialize the boxes
boxes = {
    0: ['bus'],
    1: ['book', 'suit'],
    2: ['bag', 'cross'],
    3: [],
    4: ['tea'],
    5: ['cigarette'],
    6: ['drug'],
}

# Define the moves
moves = [
    (1, None, 'book'),       # Remove the book from Box 1
    (4, 2, 'tea'),           # Move the tea from Box 4 to Box 2
    (2, None, 'cross'),      # Remove the cross from Box 2
    (2, 5, 'bag'),           # Move the bag from Box 2 to Box 5
    (None, 6, 'boot'),       # Put the boot into Box 6
    (None, 6, 'drink'),      # Put the drink into Box 6
    (None, 1, 'pipe'),       # Put the pipe into Box 1
    (None, 1, 'string'),     # Put the string into Box 1
    (None, 3, 'disk'),       # Put the disk into Box 3
    (None, 3, 'note'),       # Put the note into Box 3
    (None, 3, 'pot'),        # Put the pot into Box 3
    (1, None, 'string'),     # Remove the string from Box 1
    (1, None, 'suit'),       # Remove the suit from Box 1
    (2, 5, 'tea'),           # Move the tea from Box 2 to Box 5
    (1, None, 'pipe'),       # Remove the pipe from Box 1
    (3, 2, 'pot'),           # Move the pot from Box 3 to Box 2
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