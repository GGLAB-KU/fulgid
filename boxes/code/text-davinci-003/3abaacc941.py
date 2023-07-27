# Initialize the boxes
boxes = {
    0: ['block', 'sheet', 'tape'],
    1: ['note'],
    2: [],
    3: [],
    4: [],
    5: ['brick'],
    6: ['drug', 'game'],
}

# Define the moves
moves = [
    (1, 6, 'note'),         # Move the note from Box 1 to Box 6
    (None, 4, 'flower'),    # Put the flower into Box 4
    (6, 1, 'note'),         # Move the note from Box 6 to Box 1
    (6, 5, 'game'),         # Move the game from Box 6 to Box 5
    (None, 2, 'computer'),  # Put the computer into Box 2
    (None, 2, 'shoe'),      # Put the shoe into Box 2
    (6, None, 'drug'),      # Remove the drug from Box 6
    (4, 5, 'flower'),       # Move the flower from Box 4 to Box 5
    (None, 6, 'paper'),     # Put the paper into Box 6
    (None, 6, 'shirt'),     # Put the shirt into Box 6
    (1, None, 'note'),      # Remove the note from Box 1
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