# Initialize the boxes
boxes = {
    0: ['crown', 'magazine', 'sheet'],
    1: ['document'],
    2: ['cigarette'],
    3: ['chemical', 'drug'],
    4: ['ring'],
    5: ['brick', 'wire'],
    6: ['game', 'television', 'wheel'],
}

# Define the moves
moves = [
    (1, 5, 'document'),     # Move the document from Box 1 to Box 5
    (None, 2, 'bag'),       # Put the bag into Box 2
    (None, 2, 'medicine'),  # Put the medicine into Box 2
    (6, None, 'television'), # Remove the television from Box 6
    (3, None, 'chemical'),  # Remove the chemical from Box 3
    (3, None, 'drug'),      # Remove the drug from Box 3
    (None, 4, 'stone'),     # Put the stone into Box 4
    (6, None, 'wheel'),     # Remove the wheel from Box 6
    (6, None, 'game'),      # Remove the game from Box 6
    (None, 6, 'branch'),    # Put the branch into Box 6
    (2, None, 'bag'),       # Remove the bag from Box 2
    (2, None, 'medicine'),  # Remove the medicine from Box 2
    (6, 3, 'branch'),       # Move the branch from Box 6 to Box 3
    (3, None, 'branch'),    # Remove the branch from Box 3
    (2, 1, 'cigarette'),    # Move the cigarette from Box 2 to Box 1
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