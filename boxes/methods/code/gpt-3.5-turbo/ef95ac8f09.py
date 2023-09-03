# Initialize the boxes
boxes = {
    0: ['pipe'],
    1: ['disk', 'shell'],
    2: ['cream', 'key'],
    3: ['card', 'letter'],
    4: ['fan', 'string', 'wheel'],
    5: ['coat', 'egg', 'rose'],
    6: ['knife', 'plate'],
}

# Define the moves
moves = [
    (None, 6, 'machine'),       # Put the machine into Box 6
    (None, 3, 'seed'),          # Put the seed into Box 3
    (3, None, 'seed'),          # Remove the seed from Box 3
    (6, None, 'knife'),         # Remove the knife from Box 6
    (4, None, 'fan'),           # Remove the fan from Box 4
    (4, None, 'string'),        # Remove the string from Box 4
    (0, None, 'pipe'),          # Remove the pipe from Box 0
    (3, None, 'letter'),        # Remove the letter from Box 3
    (3, None, 'card'),          # Remove the card from Box 3
    (None, 3, 'camera'),        # Put the camera into Box 3
    (None, 3, 'medicine'),      # Put the medicine into Box 3
    (None, 3, 'paper'),         # Put the paper into Box 3
    (2, None, 'cream'),         # Remove the cream from Box 2
    (None, 4, 'cream'),         # Put the cream into Box 4
    (None, 4, 'ring'),          # Put the ring into Box 4
    (3, None, 'paper')          # Remove the paper from Box 3
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