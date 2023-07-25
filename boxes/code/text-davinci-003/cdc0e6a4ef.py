# Initialize the boxes
boxes = {
    0: ['coat'],
    1: ['wheel'],
    2: ['magazine'],
    3: ['boat', 'dish', 'plane'],
    4: [],
    5: [],
    6: ['book'],
}

# Define the moves
moves = [
    (0, None, 'coat'),       # Remove the coat from Box 0
    (1, None, 'wheel'),      # Remove the wheel from Box 1
    (2, None, 'magazine'),   # Remove the magazine from Box 2
    (3, None, 'boat'),       # Remove the boat from Box 3
    (3, None, 'dish'),       # Remove the dish from Box 3
    (3, None, 'plane'),      # Remove the plane from Box 3
    (None, 4, 'coat'),       # Put the coat into Box 4
    (None, 5, 'wheel'),      # Put the wheel into Box 5
    (None, 5, 'magazine'),   # Put the magazine into Box 5
    (None, 3, 'boat'),       # Put the boat into Box 3
    (None, 3, 'dish'),       # Put the dish into Box 3
    (None, 3, 'plane'),      # Put the plane into Box 3
    (6, None, 'book')        # Remove the book from Box 6
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