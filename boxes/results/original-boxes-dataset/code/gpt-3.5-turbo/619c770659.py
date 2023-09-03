# Initialize the boxes
boxes = {
    0: ['coat'],
    1: ['boat', 'wire'],
    2: ['cash'],
    3: ['plate'],
    4: ['milk', 'sheet'],
    5: ['ball', 'bomb', 'creature'],
    6: ['rose'],
}

# Define the moves
moves = [
    (None, 6, 'ice'),       # Put the ice into Box 6
    (None, 6, 'plant'),     # Put the plant into Box 6
    (None, 3, 'map'),       # Put the map into Box 3
    (1, None, 'wire'),      # Remove the wire from Box 1
    (0, None, 'coat'),      # Remove the coat from Box 0
    (4, None, 'sheet'),     # Remove the sheet from Box 4
    (5, None, 'bomb'),      # Remove the bomb from Box 5
    (1, 0, 'boat'),         # Move the boat from Box 1 to Box 0
    (0, 4, 'boat'),         # Move the boat from Box 0 to Box 4
    (6, None, 'plant'),     # Remove the plant from Box 6
    (6, None, 'rose'),      # Remove the rose from Box 6
    (2, 6, 'cash'),         # Move the cash from Box 2 to Box 6
    (5, 0, 'ball'),         # Move the ball from Box 5 to Box 0
    (5, 0, 'creature'),     # Move the creature from Box 5 to Box 0
    (None, 2, 'document'),  # Put the document into Box 2
    (None, 2, 'ticket')     # Put the ticket into Box 2
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