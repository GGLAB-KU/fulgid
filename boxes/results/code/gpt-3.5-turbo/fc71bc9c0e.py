# Initialize the boxes
boxes = {
    0: ['bread', 'paper', 'watch'],
    1: ['bomb', 'cake', 'newspaper'],
    2: ['key', 'milk'],
    3: ['apple', 'bill', 'fish'],
    4: ['brain', 'magazine', 'seed'],
    5: [],
    6: ['file', 'plant', 'rose'],
}

# Define the moves
moves = [
    (2, None, 'milk'),       # Remove the milk from Box 2
    (2, None, 'key'),        # Remove the key from Box 2
    (None, 2, 'ticket'),     # Put the ticket into Box 2
    (1, 5, 'cake'),          # Move the cake from Box 1 to Box 5
    (1, 5, 'newspaper'),     # Move the newspaper from Box 1 to Box 5
    (3, 1, 'fish'),          # Move the fish from Box 3 to Box 1
    (3, None, 'apple'),      # Remove the apple from Box 3
    (3, None, 'bill'),       # Remove the bill from Box 3
    (6, None, 'file'),       # Remove the file from Box 6
    (6, None, 'plant'),      # Remove the plant from Box 6
    (6, None, 'rose')        # Remove the rose from Box 6
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