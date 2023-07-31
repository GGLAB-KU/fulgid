# Initialize the boxes
boxes = {
    0: ['guitar', 'magazine', 'picture'],
    1: ['plate'],
    2: ['bell', 'branch', 'medicine'],
    3: ['boat', 'key', 'paper'],
    4: ['cup', 'tea', 'wheel'],
    5: ['bill'],
    6: ['shirt'],
}

# Define the moves
moves = [
    (6, 1, 'shirt'),        # Move the shirt from Box 6 to Box 1
    (2, None, 'bell'),      # Remove the bell from Box 2
    (2, None, 'branch'),    # Remove the branch from Box 2
    (None, 1, 'drug'),      # Put the drug into Box 1
    (None, 6, 'watch'),     # Put the watch into Box 6
    (6, None, 'watch'),     # Remove the watch from Box 6
    (4, 5, 'cup'),          # Move the cup from Box 4 to Box 5
    (4, 5, 'tea')           # Move the tea from Box 4 to Box 5
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