# Initialize the boxes
boxes = {
    0: ['bill', 'rock', 'ticket'],
    1: ['branch'],
    2: ['cigarette', 'fan', 'flower'],
    3: ['bone', 'suit'],
    4: ['car'],
    5: [],
    6: ['beer', 'meat', 'tie'],
}

# Define the moves
moves = [
    (0, 4, 'bill'),         # Move the bill from Box 0 to Box 4
    (0, 4, 'ticket'),       # Move the ticket from Box 0 to Box 4
    (2, None, 'fan'),       # Remove the fan from Box 2
    (2, None, 'flower'),    # Remove the flower from Box 2
    (2, None, 'cigarette'), # Remove the cigarette from Box 2
    (6, None, 'meat'),      # Remove the meat from Box 6
    (1, None, 'branch'),    # Remove the branch from Box 1
    (6, 1, 'beer'),         # Move the beer from Box 6 to Box 1
    (1, 3, 'beer'),         # Move the beer from Box 1 to Box 3
    (3, 6, 'bone'),         # Move the bone from Box 3 to Box 6
    (3, 6, 'suit'),         # Move the suit from Box 3 to Box 6
    (None, 1, 'egg'),       # Put the egg into Box 1
    (None, 1, 'radio'),     # Put the radio into Box 1
    (6, None, 'suit'),      # Remove the suit from Box 6
    (6, None, 'tie')        # Remove the tie from Box 6
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