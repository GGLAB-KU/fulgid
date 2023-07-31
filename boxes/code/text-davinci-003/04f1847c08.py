# Initialize the boxes
boxes = {
    0: ['painting'],
    1: ['camera'],
    2: [],
    3: ['newspaper', 'television', 'train'],
    4: ['coffee'],
    5: [],
    6: ['dish', 'ice', 'phone'],
}

# Define the moves
moves = [
    (0, None, 'painting'),   # Remove the painting from Box 0
    (None, 2, 'creature'),   # Put the creature into Box 2
    (None, 2, 'apple'),      # Put the apple into Box 2
    (2, None, 'apple'),      # Remove the apple from Box 2
    (2, None, 'creature'),   # Remove the creature from Box 2
    (3, 2, 'newspaper'),     # Move the newspaper from Box 3 to Box 2
    (3, None, 'train'),      # Remove the train from Box 3
    (6, 5, 'phone'),         # Move the phone from Box 6 to Box 5
    (6, 3, 'ice'),           # Move the ice from Box 6 to Box 3
    (5, 1, 'phone'),         # Move the phone from Box 5 to Box 1
    (2, None, 'newspaper'),  # Remove the newspaper from Box 2
    (None, 3, 'file')        # Put the file into Box 3
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