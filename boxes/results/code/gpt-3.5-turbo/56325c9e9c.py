# Initialize the boxes
boxes = {
    0: ['bone', 'branch', 'wire'],
    1: ['coat', 'radio'],
    2: ['crown', 'milk', 'suit'],
    3: [],
    4: ['boot', 'hat', 'rose'],
    5: ['computer', 'medicine', 'rock'],
    6: ['egg'],
}

# Define the moves
moves = [
    (5, None, 'computer'),  # Remove the computer from Box 5
    (4, 1, 'rose'),         # Move the rose from Box 4 to Box 1
    (2, None, 'milk'),      # Remove the milk from Box 2
    (2, None, 'suit'),      # Remove the suit from Box 2
    (None, 5, 'cake')       # Put the cake into Box 5
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