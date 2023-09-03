# Initialize the boxes
boxes = {
    0: ['boat', 'car', 'milk'],
    1: ['ball', 'boot', 'glass'],
    2: [],
    3: ['drink'],
    4: ['bowl', 'leaf', 'tape'],
    5: ['string', 'suit'],
    6: ['clock', 'wire'],
}

# Define the moves
moves = [
    (0, None, 'boat'),    # Remove the boat from Box 0
    (0, None, 'car'),     # Remove the car from Box 0
    (0, None, 'milk'),    # Remove the milk from Box 0
    (1, None, 'ball'),    # Remove the ball from Box 1
    (1, None, 'boot'),    # Remove the boot from Box 1
    (1, None, 'glass'),   # Remove the glass from Box 1
    (4, None, 'bowl'),    # Remove the bowl from Box 4
    (4, None, 'leaf'),    # Remove the leaf from Box 4
    (4, None, 'tape'),    # Remove the tape from Box 4
    (5, None, 'string'),  # Remove the string from Box 5
    (5, None, 'suit'),    # Remove the suit from Box 5
    (6, None, 'clock'),   # Remove the clock from Box 6
    (6, None, 'wire'),    # Remove the wire from Box 6
    (None, 3, 'drink'),   # Put the drink into Box 3
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