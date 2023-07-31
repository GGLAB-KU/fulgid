# Initialize the boxes
boxes = {
    0: ['bus', 'cross', 'tape'],
    1: [],
    2: ['jacket'],
    3: [],
    4: ['guitar', 'plane'],
    5: ['camera', 'plant'],
    6: ['fig'],
}

# Define the moves
moves = [
    (0, None, 'tape'),       # Remove the tape from Box 0
    (2, None, 'jacket'),     # Remove the jacket from Box 2
    (None, 5, 'ball'),       # Put the ball into Box 5
    (5, 1, 'camera'),        # Move the camera from Box 5 to Box 1
    (None, 3, 'bill'),       # Put the bill into Box 3
    (1, None, 'camera'),     # Remove the camera from Box 1
    (6, 4, 'fig'),           # Move the fig from Box 6 to Box 4
    (None, 1, 'apple'),      # Put the apple into Box 1
    (None, 1, 'branch'),     # Put the branch into Box 1
    (None, 1, 'tea'),        # Put the tea into Box 1
    (0, 2, 'cross'),         # Move the cross from Box 0 to Box 2
    (3, 0, 'bill')           # Move the bill from Box 3 to Box 0
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