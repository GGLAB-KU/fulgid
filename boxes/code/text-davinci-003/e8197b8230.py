# Initialize the boxes
boxes = {
    0: ['file'],
    1: ['cream', 'plane', 'tie'],
    2: ['bag', 'chemical', 'rock'],
    3: ['computer', 'gift', 'medicine'],
    4: ['bill', 'bone', 'jacket'],
    5: ['shoe'],
    6: ['ball', 'bowl'],
}

# Define the moves
moves = [
    (4, None, 'bill'),      # Remove the bill from Box 4
    (4, None, 'jacket'),    # Remove the jacket from Box 4
    (None, 0, 'disk')       # Put the disk into Box 0
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