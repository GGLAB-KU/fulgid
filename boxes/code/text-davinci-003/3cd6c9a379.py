# Initialize the boxes
boxes = {
    0: [],
    1: ['book'],
    2: ['ball', 'glass'],
    3: ['tissue'],
    4: ['cash', 'letter', 'seed'],
    5: ['flower', 'game', 'leaf'],
    6: ['bowl', 'bread', 'phone'],
}

# Define the moves
moves = [
    (1, None, 'book'),    # Remove the book from Box 1
    (2, None, 'glass'),   # Remove the glass from Box 2
    (6, None, 'bread'),   # Remove the bread from Box 6
    (4, 0, 'cash'),       # Move the cash from Box 4 to Box 0
    (4, 0, 'seed'),       # Move the seed from Box 4 to Box 0
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