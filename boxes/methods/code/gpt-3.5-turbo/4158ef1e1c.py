# Initialize the boxes
boxes = {
    0: ['brain', 'crown', 'fish'],
    1: ['apple'],
    2: ['game'],
    3: ['gift'],
    4: ['beer', 'computer', 'cross'],
    5: ['jacket', 'tea', 'tie'],
    6: ['cash', 'newspaper', 'plant'],
}

# Define the moves
moves = [
    (6, None, 'cash'),       # Remove the cash from Box 6
    (6, None, 'newspaper'),  # Remove the newspaper from Box 6
    (6, None, 'plant'),      # Remove the plant from Box 6
    (2, None, 'game'),       # Remove the game from Box 2
    (1, 2, 'apple'),         # Move the apple from Box 1 to Box 2
    (2, None, 'apple'),      # Remove the apple from Box 2
    (0, None, 'brain'),      # Remove the brain from Box 0
    (0, None, 'fish'),       # Remove the fish from Box 0
    (5, None, 'tie'),        # Remove the tie from Box 5
    (5, None, 'jacket'),     # Remove the jacket from Box 5
    (None, 1, 'bell'),       # Put the bell into Box 1
    (6, 0, 'apple'),         # Put the apple into Box 6
    (0, 2, 'crown'),         # Move the crown from Box 0 to Box 2
    (6, 0, 'apple'),         # Move the apple from Box 6 to Box 0
    (0, None, 'apple'),      # Remove the apple from Box 0
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