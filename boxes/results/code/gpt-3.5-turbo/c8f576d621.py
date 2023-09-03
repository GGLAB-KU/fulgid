# Initialize the boxes
boxes = {
    0: [],
    1: ['guitar', 'knife'],
    2: ['cross'],
    3: ['branch'],
    4: [],
    5: ['apple', 'bill', 'magazine'],
    6: ['bone', 'leaf', 'tape'],
}

# Define the moves
moves = [
    (1, None, 'knife'),     # Remove the knife from Box 1
    (2, 4, 'cross'),        # Move the cross from Box 2 to Box 4
    (4, 3, 'cross'),        # Move the cross from Box 4 to Box 3
    (3, 4, 'cross'),        # Move the cross from Box 3 to Box 4
    (3, None, 'branch'),    # Remove the branch from Box 3
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