# Initialize the boxes
boxes = {
    0: ['cream', 'phone'],
    1: [],
    2: ['cross', 'gift', 'plate'],
    3: ['ball', 'document'],
    4: ['bag', 'jacket', 'rose'],
    5: ['ice', 'knife'],
    6: ['egg'],
}

# Define the moves
moves = [
    (6, 0, 'egg'),       # Move the egg from Box 6 to Box 0
    (5, 6, 'knife'),     # Move the knife from Box 5 to Box 6
    (4, None, 'rose'),   # Remove the rose from Box 4
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