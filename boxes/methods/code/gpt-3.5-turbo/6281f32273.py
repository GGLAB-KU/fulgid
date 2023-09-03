# Initialize the boxes
boxes = {
    0: ['dress', 'suit', 'tape'],
    1: ['apple', 'note'],
    2: ['cash', 'coat', 'jacket'],
    3: ['file'],
    4: [],
    5: [],
    6: ['engine'],
}

# Define the moves
moves = [
    (0, None, 'suit'),       # Remove the suit from Box 0
    (2, None, 'coat'),       # Remove the coat from Box 2
    (2, None, 'jacket'),     # Remove the jacket from Box 2
    (0, None, 'tape'),       # Remove the tape from Box 0
    (1, 0, 'apple'),         # Move the apple from Box 1 to Box 0
    (None, 5, 'brick'),      # Put the brick into Box 5
    (3, 0, 'file'),          # Move the file from Box 3 to Box 0
    (2, None, 'cash'),       # Remove the cash from Box 2
    (None, 1, 'cream'),      # Put the cream into Box 1
    (1, 5, 'cream'),         # Move the cream from Box 1 to Box 5
    (1, 5, 'note')           # Move the note from Box 1 to Box 5
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