# Initialize the boxes
boxes = {
    0: ['ball', 'bread'],
    1: [],
    2: ['bottle', 'cash', 'creature'],
    3: ['engine', 'medicine', 'tissue'],
    4: ['fig', 'rose'],
    5: ['bell'],
    6: ['guitar'],
}

# Define the moves
moves = [
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