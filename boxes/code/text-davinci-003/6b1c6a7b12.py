# Initialize the boxes
boxes = {
    0: ['cheese', 'disk'],
    1: ['brain', 'cake', 'rose'],
    2: ['crown', 'shell'],
    3: ['coffee', 'painting'],
    4: ['bill', 'flower', 'plane'],
    5: ['coat', 'glass'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'painting'),   # Remove the painting from Box 3
    (None, 0, 'tie'),        # Put the tie into Box 0
    (2, None, 'crown'),      # Remove the crown from Box 2
    (1, 3, 'brain'),         # Move the brain from Box 1 to Box 3
    (1, 3, 'rose'),          # Move the rose from Box 1 to Box 3
    (5, None, 'coat'),       # Remove the coat from Box 5
    (4, None, 'bill'),       # Remove the bill from Box 4
    (None, 1, 'newspaper'),  # Put the newspaper into Box 1
    (3, None, 'brain'),      # Remove the brain from Box 3
    (3, None, 'rose'),       # Remove the rose from Box 3
    (5, None, 'glass'),      # Remove the glass from Box 5
    (4, 3, 'flower'),        # Move the flower from Box 4 to Box 3
    (2, None, 'shell'),      # Remove the shell from Box 2
    (3, None, 'flower'),     # Remove the flower from Box 3
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