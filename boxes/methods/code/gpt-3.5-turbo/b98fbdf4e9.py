# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['boat'],
    3: ['drug'],
    4: ['chemical', 'mirror', 'shell'],
    5: ['creature', 'painting', 'rock'],
    6: ['block'],
}

# Define the moves
moves = [
    (None, 0, 'bread'),         # Put the bread into Box 0
    (None, 0, 'pipe'),          # Put the pipe into Box 0
    (6, 2, 'block'),            # Move the block from Box 6 to Box 2
    (5, None, 'creature'),      # Remove the creature from Box 5
    (5, None, 'painting'),      # Remove the painting from Box 5
    (5, 6, 'rock'),             # Move the rock from Box 5 to Box 6
    (None, 0, 'cup'),           # Put the cup into Box 0
    (None, 6, 'cigarette'),     # Put the cigarette into Box 6
    (6, 3, 'cigarette'),        # Move the cigarette from Box 6 to Box 3
    (6, 3, 'rock'),             # Move the rock from Box 6 to Box 3
    (4, 6, 'chemical'),         # Move the chemical from Box 4 to Box 6
    (4, 6, 'mirror'),           # Move the mirror from Box 4 to Box 6
    (4, 6, 'shell'),            # Move the shell from Box 4 to Box 6
    (6, 4, 'chemical'),         # Move the chemical from Box 6 to Box 4
    (6, 4, 'shell')             # Move the shell from Box 6 to Box 4
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