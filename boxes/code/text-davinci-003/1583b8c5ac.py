# Initialize the boxes
boxes = {
    0: ['jacket', 'tape'],
    1: ['ring'],
    2: ['dish'],
    3: ['drink'],
    4: ['ball', 'fan', 'file'],
    5: ['ice', 'radio'],
    6: ['leaf', 'string'],
}

# Define the moves
moves = [
    (4, None, 'tape'),       # Remove the tape from Box 4
    (4, None, 'fan'),        # Remove the fan from Box 4
    (4, None, 'file'),       # Remove the file from Box 4
    (5, None, 'ice'),        # Remove the ice from Box 5
    (5, None, 'radio'),      # Remove the radio from Box 5
    (6, None, 'leaf'),       # Remove the leaf from Box 6
    (6, None, 'string'),     # Remove the string from Box 6
    (None, 0, 'tape'),       # Put the tape into Box 0
    (None, 0, 'fan'),        # Put the fan into Box 0
    (None, 0, 'file'),       # Put the file into Box 0
    (None, 0, 'ice'),        # Put the ice into Box 0
    (None, 0, 'radio'),      # Put the radio into Box 0
    (None, 0, 'leaf'),       # Put the leaf into Box 0
    (None, 0, 'string'),     # Put the string into Box 0
    (None, 3, 'jacket'),     # Put the jacket into Box 3
    (None, 3, 'drink'),      # Put the drink into Box 3
    (None, 3, 'ring'),       # Put the ring into Box 3
    (None, 3, 'dish'),       # Put the dish into Box 3
    (None, 3, 'ball')        # Put the ball into Box 3
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