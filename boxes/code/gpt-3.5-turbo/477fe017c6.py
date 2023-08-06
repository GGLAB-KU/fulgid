# Initialize the boxes
boxes = {
    0: ['clock', 'magazine'],
    1: ['chemical', 'letter', 'string'],
    2: ['computer', 'picture', 'tissue'],
    3: [],
    4: ['block', 'glass', 'tea'],
    5: ['milk'],
    6: ['boot', 'wheel'],
}

# Define the moves
moves = [
    (6, None, 'boot'),       # Remove the boot from Box 6
    (5, 6, 'milk'),          # Move the milk from Box 5 to Box 6
    (1, None, 'chemical'),   # Remove the chemical from Box 1
    (1, None, 'string'),     # Remove the string from Box 1
    (1, 5, 'letter'),        # Move the letter from Box 1 to Box 5
    (2, 1, 'picture'),       # Move the picture from Box 2 to Box 1
    (2, 1, 'tissue'),        # Move the tissue from Box 2 to Box 1
    (0, None, 'magazine'),   # Remove the magazine from Box 0
    (0, None, 'clock'),      # Remove the clock from Box 0
    (None, 2, 'cash'),       # Put the cash into Box 2
    (None, 2, 'creature'),   # Put the creature into Box 2
    (2, None, 'pipe'),       # Put the pipe into Box 0
    (2, None, 'creature')    # Remove the creature from Box 2
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