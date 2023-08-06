# Initialize the boxes
boxes = {
    0: [],
    1: ['bottle', 'knife'],
    2: ['document'],
    3: [],
    4: ['clock', 'medicine', 'stone'],
    5: ['boot', 'bread', 'shell'],
    6: ['bowl', 'mirror'],
}

# Define the moves
moves = [
    (4, 2, 'clock'),       # Move the clock from Box 4 to Box 2
    (4, 2, 'medicine'),    # Move the medicine from Box 4 to Box 2
    (None, 6, 'guitar'),   # Put the guitar into Box 6
    (4, None, 'stone'),    # Remove the stone from Box 4
    (None, 0, 'ice'),      # Put the ice into Box 0
    (None, 0, 'creature'), # Put the creature into Box 0
    (None, 0, 'machine')   # Put the machine into Box 0
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