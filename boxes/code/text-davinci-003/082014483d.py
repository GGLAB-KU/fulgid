# Initialize the boxes
boxes = {
    0: ['chemical', 'magazine'],
    1: ['wire'],
    2: ['boat', 'book', 'drink'],
    3: ['ball', 'fan', 'gift'],
    4: ['dish'],
    5: ['file'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'ball'),       # Remove the ball from Box 3
    (2, None, 'boat'),       # Remove the boat from Box 2
    (2, None, 'book'),       # Remove the book from Box 2
    (0, 1, 'magazine'),      # Move the magazine from Box 0 to Box 1
    (1, None, 'magazine'),   # Remove the magazine from Box 1
    (1, None, 'wire'),       # Remove the wire from Box 1
    (None, 1, 'ticket'),     # Put the ticket into Box 1
    (4, 1, 'dish'),          # Move the dish from Box 4 to Box 1
    (None, 4, 'watch'),      # Put the watch into Box 4
    (1, 4, 'dish'),          # Move the dish from Box 1 to Box 4
    (2, 6, 'drink'),         # Move the drink from Box 2 to Box 6
    (5, 2, 'file'),          # Move the file from Box 5 to Box 2
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