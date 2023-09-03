# Initialize the boxes
boxes = {
    0: ['computer', 'sheet', 'stone'],
    1: ['cup', 'fish'],
    2: ['brick', 'coffee', 'knife'],
    3: ['ice', 'machine'],
    4: ['fan', 'magazine'],
    5: [],
    6: ['boat', 'chemical'],
}

# Define the moves
moves = [
    (4, 6, 'fan'),       # Move the fan from Box 4 to Box 6
    (3, None, 'ice'),    # Remove the ice from Box 3
    (1, None, 'cup'),    # Remove the cup from Box 1
    (1, 5, 'fish'),      # Move the fish from Box 1 to Box 5
    (3, 1, 'machine'),   # Move the machine from Box 3 to Box 1
    (4, 5, 'magazine'),  # Move the magazine from Box 4 to Box 5
    (1, None, 'machine'),  # Remove the machine from Box 1
    (5, 3, 'magazine'),  # Move the magazine from Box 5 to Box 3
    (0, None, 'computer'),  # Remove the computer from Box 0
    (0, None, 'sheet'),  # Remove the sheet from Box 0
    (3, None, 'magazine'),  # Remove the magazine from Box 3
    (0, None, 'stone'),  # Remove the stone from Box 0
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