# Initialize the boxes
boxes = {
    0: ['knife'],
    1: ['drug', 'file', 'milk'],
    2: ['beer'],
    3: [],
    4: ['radio', 'tie', 'wire'],
    5: ['bowl'],
    6: ['cross', 'plane'],
}

# Define the moves
moves = [
    (0, None, 'knife'),     # Remove the knife from Box 0
    (5, None, 'bowl'),      # Remove the bowl from Box 5
    (6, 3, 'cross'),        # Move the cross from Box 6 to Box 3
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