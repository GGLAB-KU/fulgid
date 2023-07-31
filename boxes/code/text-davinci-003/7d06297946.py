# Initialize the boxes
boxes = {
    0: ['crown'],
    1: ['cake', 'cup', 'picture'],
    2: ['tie'],
    3: ['computer', 'rose', 'tissue'],
    4: ['egg'],
    5: ['document', 'fish'],
    6: ['plate'],
}

# Define the moves
moves = [
    (2, None, 'tie'),       # Remove the tie from Box 2
    (3, 0, 'rose'),         # Move the rose from Box 3 to Box 0
    (3, 0, 'tissue'),       # Move the tissue from Box 3 to Box 0
    (None, 6, 'bus'),       # Put the bus into Box 6
    (None, 6, 'drink'),     # Put the drink into Box 6
    (1, None, 'cake'),      # Remove the cake from Box 1
    (1, None, 'cup'),       # Remove the cup from Box 1
    (0, None, 'crown'),     # Remove the crown from Box 0
    (0, None, 'rose'),      # Remove the rose from Box 0
    (0, None, 'tissue'),    # Remove the tissue from Box 0
    (None, 3, 'card'),      # Put the card into Box 3
    (None, 3, 'ice')        # Put the ice into Box 3
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