# Initialize the boxes
boxes = {
    0: ['key', 'map', 'watch'],
    1: ['milk', 'picture', 'plate'],
    2: ['card', 'guitar', 'ring'],
    3: ['letter', 'paper'],
    4: ['bomb', 'leaf'],
    5: ['chemical', 'gift', 'magazine'],
    6: ['dress', 'train'],
}

# Define the moves
moves = [
    (6, None, 'train'),       # Remove the train from Box 6
    (2, None, 'ring'),        # Remove the ring from Box 2
    (6, None, 'dress'),       # Remove the dress from Box 6
    (None, 4, 'document'),    # Put the document into Box 4
    (5, 2, 'magazine'),       # Move the magazine from Box 5 to Box 2
    (5, None, 'chemical'),    # Remove the chemical from Box 5
    (1, None, 'picture'),     # Remove the picture from Box 1
    (1, 3, 'plate'),          # Move the plate from Box 1 to Box 3
    (0, None, 'key'),         # Remove the key from Box 0
    (0, None, 'map'),         # Remove the map from Box 0
    (None, 5, 'ticket'),      # Put the ticket into Box 5
    (2, 0, 'magazine'),       # Move the magazine from Box 2 to Box 0
    (0, None, 'watch')        # Remove the watch from Box 0
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