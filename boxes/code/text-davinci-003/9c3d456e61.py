# Initialize the boxes
boxes = {
    0: ['coffee', 'fish', 'gift'],
    1: ['coat', 'shoe'],
    2: ['ball', 'computer'],
    3: ['leaf', 'string'],
    4: ['branch', 'letter', 'shell'],
    5: ['document'],
    6: ['bread', 'clock', 'wheel'],
}

# Define the moves
moves = [
    (3, None, 'leaf'),       # Remove the leaf from Box 3
    (0, None, 'fish'),       # Remove the fish from Box 0
    (6, None, 'bread'),      # Remove the bread from Box 6
    (6, None, 'clock'),      # Remove the clock from Box 6
    (2, 0, 'ball'),          # Move the ball from Box 2 to Box 0
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