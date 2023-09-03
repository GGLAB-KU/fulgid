# Initialize the boxes
boxes = {
    0: ['fan', 'television'],
    1: ['brain', 'fig'],
    2: ['bone', 'watch'],
    3: ['apple', 'coffee', 'train'],
    4: ['shell', 'shirt'],
    5: ['bill', 'shoe'],
    6: ['key', 'rose'],
}

# Define the moves
moves = [
    (6, 5, 'key'),         # Move the key from Box 6 to Box 5
    (6, 0, 'rose'),        # Move the rose from Box 6 to Box 0
    (5, None, 'key'),      # Remove the key from Box 5
    (5, None, 'shoe'),     # Remove the shoe from Box 5
    (None, 6, 'boat'),     # Put the boat into Box 6
    (0, None, 'fan'),      # Remove the fan from Box 0
    (0, None, 'rose'),     # Remove the rose from Box 0
    (2, None, 'bone'),     # Remove the bone from Box 2
    (None, 0, 'rock'),     # Put the rock into Box 0
    (3, None, 'apple'),    # Remove the apple from Box 3
    (3, None, 'train'),    # Remove the train from Box 3
    (6, 0, 'boat'),        # Move the boat from Box 6 to Box 0
    (5, 2, 'bill'),        # Move the bill from Box 5 to Box 2
    (3, 4, 'coffee'),      # Move the coffee from Box 3 to Box 4
    (None, 6, 'fish'),     # Put the fish into Box 6
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