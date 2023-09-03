# Initialize the boxes
boxes = {
    0: ['chemical'],
    1: ['brick', 'engine', 'glass'],
    2: ['ball', 'fan', 'painting'],
    3: ['machine'],
    4: [],
    5: ['beer', 'stone', 'ticket'],
    6: ['bottle', 'game'],
}

# Define the moves
moves = [
    (3, None, 'machine'),       # Remove the machine from Box 3
    (6, 4, 'bottle'),           # Move the bottle from Box 6 to Box 4
    (6, 4, 'game'),             # Move the game from Box 6 to Box 4
    (4, None, 'game'),          # Remove the game from Box 4
    (None, 4, 'disk'),          # Put the disk into Box 4
    (1, 3, 'brick'),            # Move the brick from Box 1 to Box 3
    (1, 3, 'engine'),           # Move the engine from Box 1 to Box 3
    (3, None, 'brick'),         # Remove the brick from Box 3
    (3, None, 'engine'),        # Remove the engine from Box 3
    (0, None, 'chemical'),      # Remove the chemical from Box 0
    (1, 0, 'glass'),            # Move the glass from Box 1 to Box 0
    (0, None, 'glass'),         # Remove the glass from Box 0
    (None, 3, 'medicine'),      # Put the medicine into Box 3
    (3, 1, 'medicine'),         # Move the medicine from Box 3 to Box 1
    (5, 6, 'stone'),            # Move the stone from Box 5 to Box 6
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