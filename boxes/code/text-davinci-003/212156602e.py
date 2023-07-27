# Initialize the boxes
boxes = {
    0: ['magazine'],
    1: ['disk'],
    2: ['apple', 'painting', 'wire'],
    3: [],
    4: ['boot', 'cup', 'radio'],
    5: ['camera', 'cream', 'guitar'],
    6: ['card', 'file'],
}

# Define the moves
moves = [
    (0, 1, 'magazine'),   # Move the magazine from Box 0 to Box 1
    (6, 3, 'file'),       # Move the file from Box 6 to Box 3
    (5, 1, 'guitar'),     # Move the guitar from Box 5 to Box 1
    (None, 3, 'book'),    # Put the book into Box 3
    (None, 3, 'cross'),   # Put the cross into Box 3
    (3, None, 'book'),    # Remove the book from Box 3
    (3, None, 'cross'),   # Remove the cross from Box 3
    (1, None, 'magazine'),# Remove the magazine from Box 1
    (None, 1, 'mirror'),  # Put the mirror into Box 1
    (3, None, 'file')     # Remove the file from Box 3
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