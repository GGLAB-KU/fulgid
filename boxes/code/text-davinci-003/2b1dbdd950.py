# Initialize the boxes
boxes = {
    0: ['bill', 'cream'],
    1: ['coffee', 'wheel'],
    2: ['car', 'letter', 'tape'],
    3: ['leaf', 'machine', 'watch'],
    4: ['glass', 'magazine', 'radio'],
    5: ['document', 'fan', 'plant'],
    6: ['coat'],
}

# Define the moves
moves = [
    (6, 0, 'coat'),         # Move the coat from Box 6 to Box 0
    (4, None, 'glass'),     # Remove the glass from Box 4
    (2, 4, 'car'),          # Move the car from Box 2 to Box 4
    (1, None, 'coffee'),    # Remove the coffee from Box 1
    (1, None, 'wheel'),     # Remove the wheel from Box 1
    (4, None, 'magazine'),  # Remove the magazine from Box 4
    (4, None, 'radio'),     # Remove the radio from Box 4
    (0, 1, 'bill'),         # Move the bill from Box 0 to Box 1
    (0, 1, 'coat'),         # Move the coat from Box 0 to Box 1
    (0, 1, 'cream'),        # Move the cream from Box 0 to Box 1
    (5, None, 'document'),  # Remove the document from Box 5
    (1, None, 'bill'),      # Remove the bill from Box 1
    (3, None, 'leaf'),      # Remove the leaf from Box 3
    (3, None, 'watch'),     # Remove the watch from Box 3
    (4, 5, 'car'),          # Move the car from Box 4 to Box 5
    (None, 6, 'cheese'),    # Put the cheese into Box 6
    (None, 6, 'leaf'),      # Put the leaf into Box 6
    (None, 6, 'meat')       # Put the meat into Box 6
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