# Initialize the boxes
boxes = {
    0: [],
    1: ['dress', 'key', 'plate'],
    2: [],
    3: ['game', 'tie', 'train'],
    4: ['jacket', 'shell'],
    5: ['computer', 'crown', 'suit'],
    6: ['disk', 'wheel'],
}

# Define the moves
moves = [
    (None, 0, 'chemical'),     # Put the chemical into Box 0
    (None, 0, 'egg'),          # Put the egg into Box 0
    (None, 6, 'shirt'),        # Put the shirt into Box 6
    (None, 4, 'pot'),          # Put the pot into Box 4
    (None, 2, 'cash'),         # Put the cash into Box 2
    (None, 2, 'meat'),         # Put the meat into Box 2
    (None, 2, 'paper'),        # Put the paper into Box 2
    (0, None, 'egg'),          # Remove the egg from Box 0
    (1, None, 'dress'),        # Remove the dress from Box 1
    (0, None, 'chemical'),     # Remove the chemical from Box 0
    (None, 0, 'cigarette'),    # Put the cigarette into Box 0
    (5, None, 'computer'),     # Remove the computer from Box 5
    (5, None, 'crown'),        # Remove the crown from Box 5
    (0, None, 'suit'),         # Move the suit from Box 0
    (1, None, 'suit'),         # Move the suit from Box 1
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