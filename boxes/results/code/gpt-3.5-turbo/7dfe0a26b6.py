# Initialize the boxes
boxes = {
    0: [],
    1: ['picture'],
    2: ['ball'],
    3: ['cream', 'leaf', 'train'],
    4: ['bottle'],
    5: ['creature'],
    6: ['dress'],
}

# Define the moves
moves = [
    (6, 1, 'dress'),    # Move the dress from Box 6 to Box 1
    (None, 2, 'boat'),  # Put the boat into Box 2
    (4, None, 'bottle'),  # Remove the bottle from Box 4
    (3, None, 'cream'),  # Remove the cream from Box 3
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