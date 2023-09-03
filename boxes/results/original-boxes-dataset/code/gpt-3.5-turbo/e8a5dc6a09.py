# Initialize the boxes
boxes = {
    0: ['computer', 'file', 'rock'],
    1: ['ball', 'egg', 'engine'],
    2: ['bill', 'bomb', 'brick'],
    3: ['magazine'],
    4: ['radio', 'tape'],
    5: ['coat'],
    6: ['hat'],
}

# Define the moves
moves = [
    (0, None, 'file'),      # Remove the file from Box 0
    (0, None, 'rock'),      # Remove the rock from Box 0
    (1, 6, 'egg'),          # Move the egg from Box 1 to Box 6
    (4, None, 'tape'),      # Remove the tape from Box 4
    (3, None, 'magazine'),  # Remove the magazine from Box 3
    (2, None, 'brick'),     # Remove the brick from Box 2
    (0, None, 'computer'),  # Remove the computer from Box 0
    (5, None, 'coat')       # Remove the coat from Box 5
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