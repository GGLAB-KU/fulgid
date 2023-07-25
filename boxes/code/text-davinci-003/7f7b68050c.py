# Initialize the boxes
boxes = {
    0: ['brain', 'rose'],
    1: [],
    2: ['egg'],
    3: ['cash', 'cigarette', 'train'],
    4: ['disk'],
    5: ['computer', 'drink'],
    6: ['jacket'],
}

# Define the moves
moves = [
    (None, 1, 'pot'),       # Put the pot into Box 1
    (1, 0, 'pot'),          # Move the pot from Box 1 to Box 0
    (6, None, 'jacket'),    # Remove the jacket from Box 6
    (0, None, 'brain'),     # Remove the brain from Box 0
    (0, None, 'pot'),       # Remove the pot from Box 0
    (0, None, 'rose'),      # Remove the rose from Box 0
    (None, 4, 'cake')       # Put the cake into Box 4
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