# Initialize the boxes
boxes = {
    0: ['computer', 'disk', 'newspaper'],
    1: ['bottle', 'cash'],
    2: ['bell', 'plane'],
    3: ['cheese'],
    4: ['brain', 'fig'],
    5: ['pipe'],
    6: ['dress'],
}

# Define the moves
moves = [
    (5, 3, 'pipe'),         # Move the pipe from Box 5 to Box 3
    (1, None, 'bottle'),    # Remove the bottle from Box 1
    (1, None, 'cash'),      # Remove the cash from Box 1
    (3, None, 'cheese'),    # Remove the cheese from Box 3
    (2, 6, 'bell'),         # Move the bell from Box 2 to Box 6
    (6, 4, 'dress'),        # Move the dress from Box 6 to Box 4
    (3, None, 'pipe'),      # Remove the pipe from Box 3
    (0, None, 'newspaper'), # Remove the newspaper from Box 0
    (6, None, 'bell')       # Remove the bell from Box 6
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