# Initialize the boxes
boxes = {
    0: ['flower', 'game', 'rock'],
    1: ['beer'],
    2: ['clock', 'jacket', 'radio'],
    3: ['apple', 'gift'],
    4: ['file', 'plate', 'wheel'],
    5: ['bowl'],
    6: ['egg', 'ice', 'shirt'],
}

# Define the moves
moves = [
    (1, 5, 'beer'),         # Move the beer from Box 1 to Box 5
    (5, 3, 'beer'),         # Move the beer from Box 5 to Box 3
    (None, 1, 'coffee'),    # Put the coffee into Box 1
    (0, 1, 'flower'),       # Move the flower from Box 0 to Box 1
    (0, 1, 'rock'),         # Move the rock from Box 0 to Box 1
    (4, None, 'file'),      # Remove the file from Box 4
    (4, None, 'wheel'),     # Remove the wheel from Box 4
    (5, 4, 'bowl'),         # Move the bowl from Box 5 to Box 4
    (0, None, 'game'),      # Remove the game from Box 0
    (3, None, 'apple'),     # Remove the apple from Box 3
    (3, None, 'gift'),      # Remove the gift from Box 3
    (3, 4, 'beer'),         # Move the beer from Box 3 to Box 4
    (1, None, 'coffee'),    # Remove the coffee from Box 1
    (1, None, 'flower'),    # Remove the flower from Box 1
    (6, None, 'ice'),       # Remove the ice from Box 6
    (6, None, 'shirt'),     # Remove the shirt from Box 6
    (4, 6, 'bowl'),         # Move the bowl from Box 4 to Box 6
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