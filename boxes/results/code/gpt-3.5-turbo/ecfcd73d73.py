# Initialize the boxes
boxes = {
    0: ['painting'],
    1: [],
    2: ['drug', 'game'],
    3: ['chemical', 'egg', 'pot'],
    4: ['computer', 'rose'],
    5: ['cheese', 'clock', 'coffee'],
    6: [],
}

# Define the moves
moves = [
    (None, 0, 'plate'),        # Put the plate into Box 0
    (None, 0, 'pipe'),         # Put the pipe into Box 0
    (2, 1, 'drug'),            # Move the drug from Box 2 to Box 1
    (2, 1, 'game'),            # Move the game from Box 2 to Box 1
    (3, None, 'chemical'),     # Remove the chemical from Box 3
    (3, None, 'pot'),          # Remove the pot from Box 3
    (5, None, 'cheese'),       # Remove the cheese from Box 5
    (5, None, 'clock'),        # Remove the clock from Box 5
    (5, None, 'coffee'),       # Remove the coffee from Box 5
    (3, None, 'egg'),          # Remove the egg from Box 3
    (4, None, 'rose'),         # Remove the rose from Box 4
    (None, 3, 'fan'),          # Put the fan into Box 3
    (4, 2, 'computer'),        # Move the computer from Box 4 to Box 2
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