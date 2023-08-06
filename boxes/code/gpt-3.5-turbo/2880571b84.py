# Initialize the boxes
boxes = {
    0: ['apple', 'shell', 'television'],
    1: ['brick', 'mirror', 'plane'],
    2: ['rock'],
    3: ['coffee', 'train'],
    4: [],
    5: ['clock', 'fan'],
    6: [],
}

# Define the moves
moves = [
    (None, 4, 'dish')   # Put the dish into Box 4
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