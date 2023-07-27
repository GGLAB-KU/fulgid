# Initialize the boxes
boxes = {
    0: ['car'],
    1: ['clock', 'drug', 'stone'],
    2: ['block', 'bread', 'fish'],
    3: [],
    4: ['chemical', 'cream', 'crown'],
    5: ['dress', 'magazine'],
    6: ['boat', 'bone'],
}

# Define the moves
moves = [
    (1, None, 'drug'),       # Remove the drug from Box 1
    (1, None, 'stone'),      # Remove the stone from Box 1
    (6, 1, 'bone'),          # Move the bone from Box 6 to Box 1
    (1, None, 'clock'),      # Remove the clock from Box 1
    (5, 1, 'magazine'),      # Move the magazine from Box 5 to Box 1
    (4, None, 'chemical'),   # Remove the chemical from Box 4
    (4, None, 'cream'),      # Remove the cream from Box 4
    (4, None, 'crown')       # Remove the crown from Box 4
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