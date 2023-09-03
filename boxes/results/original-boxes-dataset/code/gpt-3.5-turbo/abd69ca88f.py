# Initialize the boxes
boxes = {
    0: ['apple', 'fig', 'ice'],
    1: ['branch', 'creature', 'egg'],
    2: ['bone', 'watch'],
    3: ['file', 'television'],
    4: ['crown'],
    5: [],
    6: ['engine', 'phone'],
}

# Define the moves
moves = [
    (2, None, 'watch'),       # Remove the watch from Box 2
    (3, None, 'file'),        # Remove the file from Box 3
    (6, 5, 'engine'),         # Move the engine from Box 6 to Box 5
    (6, 5, 'phone'),          # Move the phone from Box 6 to Box 5
    (4, 5, 'crown'),          # Move the crown from Box 4 to Box 5
    (0, None, 'apple'),       # Remove the apple from Box 0
    (0, None, 'fig'),         # Remove the fig from Box 0
    (0, None, 'ice')          # Remove the ice from Box 0
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