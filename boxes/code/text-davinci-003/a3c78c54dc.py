# Initialize the boxes
boxes = {
    0: ['letter', 'stone'],
    1: [],
    2: ['bell', 'cash'],
    3: ['bowl', 'seed', 'tea'],
    4: ['cup'],
    5: ['knife', 'ring'],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'bell'),       # Remove the bell from Box 2
    (2, None, 'cash'),       # Remove the cash from Box 2
    (3, 2, 'bowl'),          # Move the bowl from Box 3 to Box 2
    (0, 1, 'letter'),        # Move the letter from Box 0 to Box 1
    (0, 1, 'stone'),         # Move the stone from Box 0 to Box 1
    (4, None, 'cup')         # Remove the cup from Box 4
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