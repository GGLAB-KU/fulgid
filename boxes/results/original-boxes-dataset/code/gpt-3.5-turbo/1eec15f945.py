# Initialize the boxes
boxes = {
    0: ['file'],
    1: ['bus'],
    2: ['boat', 'bottle', 'engine'],
    3: ['ball', 'cream', 'milk'],
    4: ['gift', 'pot'],
    5: ['fan'],
    6: ['boot'],
}

# Define the moves
moves = [
    (None, 6, 'game'),       # Put the game into Box 6
    (6, None, 'game'),       # Remove the game from Box 6
    (6, None, 'boot'),       # Remove the boot from Box 6
    (5, 1, 'fan'),           # Move the fan from Box 5 to Box 1
    (None, 5, 'bell'),       # Put the bell into Box 5
    (None, 5, 'coffee'),     # Put the coffee into Box 5
    (None, 5, 'jacket'),     # Put the jacket into Box 5
    (0, None, 'file'),       # Remove the file from Box 0
    (4, 1, 'gift'),          # Move the gift from Box 4 to Box 1
    (5, None, 'bell'),       # Remove the bell from Box 5
    (5, None, 'coffee'),     # Remove the coffee from Box 5
    (5, None, 'jacket'),     # Remove the jacket from Box 5
    (4, None, 'pot'),        # Remove the pot from Box 4
    (1, None, 'bus')         # Remove the bus from Box 1
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