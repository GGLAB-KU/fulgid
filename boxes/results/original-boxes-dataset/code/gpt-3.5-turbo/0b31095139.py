# Initialize the boxes
boxes = {
    0: ['apple', 'drug', 'engine'],
    1: ['newspaper'],
    2: [],
    3: ['cheese', 'hat'],
    4: ['ball'],
    5: ['bowl'],
    6: ['book'],
}

# Define the moves
moves = [
    (1, 3, 'newspaper'),    # Move the newspaper from Box 1 to Box 3
    (4, 1, 'ball'),         # Move the ball from Box 4 to Box 1
    (3, None, 'cheese'),    # Remove the cheese from Box 3
    (3, None, 'hat'),       # Remove the hat from Box 3
    (None, 2, 'suit'),      # Put the suit into Box 2
    (0, 3, 'drug'),         # Move the drug from Box 0 to Box 3
    (0, 3, 'engine'),       # Move the engine from Box 0 to Box 3
    (1, None, 'ball'),      # Remove the ball from Box 1
    (6, 0, 'book'),         # Move the book from Box 6 to Box 0
    (None, 6, 'bag'),       # Put the bag into Box 6
    (None, 6, 'dress'),     # Put the dress into Box 6
    (0, 6, 'apple'),        # Move the apple from Box 0 to Box 6
    (2, 5, 'suit'),         # Move the suit from Box 2 to Box 5
    (6, 2, 'bag'),          # Move the bag from Box 6 to Box 2
    (None, 6, 'branch')     # Put the branch into Box 6
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