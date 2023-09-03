# Initialize the boxes
boxes = {
    0: ['block', 'television', 'watch'],
    1: ['ice'],
    2: [],
    3: ['shirt'],
    4: ['card', 'engine'],
    5: ['ball'],
    6: ['brick', 'knife'],
}

# Define the moves
moves = [
    (None, 2, 'bread'),     # Put the bread into Box 2
    (None, 1, 'bowl'),      # Put the bowl into Box 1
    (3, 5, 'shirt'),        # Move the shirt from Box 3 to Box 5
    (1, 2, 'bowl'),         # Move the bowl from Box 1 to Box 2
    (1, 2, 'ice'),          # Move the ice from Box 1 to Box 2
    (6, 3, 'brick'),        # Move the brick from Box 6 to Box 3
    (None, 3, 'bill'),      # Put the bill into Box 3
    (None, 3, 'mirror'),    # Put the mirror into Box 3
    (5, None, 'shirt'),     # Remove the shirt from Box 5
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