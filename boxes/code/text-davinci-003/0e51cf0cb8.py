# Initialize the boxes
boxes = {
    0: ['tissue'],
    1: ['guitar'],
    2: [],
    3: ['letter', 'newspaper'],
    4: ['computer'],
    5: ['cake', 'paper', 'wheel'],
    6: ['cup', 'knife'],
}

# Define the moves
moves = [
    (4, 1, 'computer'),     # Move the computer from Box 4 to Box 1
    (0, None, 'tissue'),    # Remove the tissue from Box 0
    (None, 1, 'bone'),      # Put the bone into Box 1
    (3, 2, 'newspaper'),    # Move the newspaper from Box 3 to Box 2
    (5, None, 'wheel'),     # Remove the wheel from Box 5
    (None, 4, 'book')       # Put the book into Box 4
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