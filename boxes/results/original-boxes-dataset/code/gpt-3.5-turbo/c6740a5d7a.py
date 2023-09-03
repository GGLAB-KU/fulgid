# Initialize the boxes
boxes = {
    0: ['cash', 'machine'],
    1: ['cheese', 'document', 'drink'],
    2: [],
    3: ['plane'],
    4: ['seed', 'sheet', 'string'],
    5: ['note'],
    6: ['rock'],
}

# Define the moves
moves = [
    (None, 2, 'fig'),          # Put the fig into Box 2
    (5, 2, 'note'),             # Move the note from Box 5 to Box 2
    (4, None, 'seed'),          # Remove the seed from Box 4
    (4, None, 'sheet'),         # Remove the sheet from Box 4
    (6, 0, 'rock'),             # Move the rock from Box 6 to Box 0
    (0, 4, 'rock'),             # Move the rock from Box 0 to Box 4
    (2, None, 'fig'),           # Remove the fig from Box 2
    (None, 2, 'magazine'),      # Put the magazine into Box 2
    (2, None, 'magazine'),      # Remove the magazine from Box 2
    (2, None, 'note'),          # Remove the note from Box 2
    (None, 2, 'coat')           # Put the coat into Box 2
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