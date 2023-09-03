# Initialize the boxes
boxes = {
    0: ['cake', 'ice', 'television'],
    1: ['newspaper', 'ring'],
    2: ['cash'],
    3: ['plate', 'rock', 'watch'],
    4: ['engine', 'fan'],
    5: ['bill'],
    6: ['knife', 'string', 'ticket'],
}

# Define the moves
moves = [
    (1, None, 'newspaper'),   # Remove the newspaper from Box 1
    (1, None, 'ring'),        # Remove the ring from Box 1
    (6, 4, 'ticket'),         # Move the ticket from Box 6 to Box 4
    (3, None, 'rock'),        # Remove the rock from Box 3
    (3, None, 'watch'),       # Remove the watch from Box 3
    (3, None, 'plate'),       # Remove the plate from Box 3
    (6, None, 'knife'),       # Remove the knife from Box 6
    (5, None, 'bill'),        # Remove the bill from Box 5
    (None, 1, 'sheet'),       # Put the sheet into Box 1
    (None, 1, 'tissue'),      # Put the tissue into Box 1
    (4, None, 'ticket'),      # Remove the ticket from Box 4
    (None, 6, 'bill')         # Put the bill into Box 6
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