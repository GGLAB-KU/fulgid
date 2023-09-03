# Initialize the boxes
boxes = {
    0: ['leaf'],
    1: ['block', 'rose'],
    2: ['book', 'car'],
    3: ['pot'],
    4: ['apple'],
    5: ['brain', 'clock', 'egg'],
    6: ['coffee'],
}

# Define the moves
moves = [
    (1, None, 'block'),     # Remove the block from Box 1
    (1, None, 'rose'),      # Remove the rose from Box 1
    (None, 0, 'phone'),     # Put the phone into Box 0
    (5, 1, 'brain'),        # Move the brain from Box 5 to Box 1
    (5, 1, 'egg'),          # Move the egg from Box 5 to Box 1
    (6, 1, 'coffee'),       # Move the coffee from Box 6 to Box 1
    (4, None, 'apple'),     # Remove the apple from Box 4
    (3, 6, 'pot'),          # Move the pot from Box 3 to Box 6
    (1, None, 'coffee'),    # Remove the coffee from Box 1
    (1, None, 'egg'),       # Remove the egg from Box 1
    (0, None, 'phone'),     # Remove the phone from Box 0
    (None, 1, 'game'),      # Put the game into Box 1
    (6, 5, 'pot'),          # Move the pot from Box 6 to Box 5
    (None, 4, 'apple'),     # Put the apple into Box 4
    (None, 4, 'pipe'),      # Put the pipe into Box 4
    (None, 1, 'cash')       # Put the cash into Box 1
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