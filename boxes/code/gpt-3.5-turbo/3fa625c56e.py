# Initialize the boxes
boxes = {
    0: ['magazine'],
    1: ['boot', 'cheese', 'chemical'],
    2: [],
    3: ['bowl', 'glass', 'hat'],
    4: ['branch', 'drug', 'egg'],
    5: ['tie'],
    6: ['pipe', 'stone'],
}

# Define the moves
moves = [
    (1, 2, 'boot'),         # Move the boot from Box 1 to Box 2
    (1, 2, 'cheese'),       # Move the cheese from Box 1 to Box 2
    (1, 2, 'chemical'),     # Move the chemical from Box 1 to Box 2
    (6, None, 'stone'),     # Remove the stone from Box 6
    (None, 6, 'meat'),      # Put the meat into Box 6
    (None, 6, 'string'),    # Put the string into Box 6
    (None, 1, 'medicine'),  # Put the medicine into Box 1
    (5, None, 'tie'),       # Remove the tie from Box 5
    (1, None, 'medicine'),  # Remove the medicine from Box 1
    (None, 1, 'cup'),       # Put the cup into Box 1
    (0, None, 'magazine'),  # Remove the magazine from Box 0
    (1, 5, 'cup'),          # Move the cup from Box 1 to Box 5
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