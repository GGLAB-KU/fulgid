# Initialize the boxes
boxes = {
    0: ['document', 'engine'],
    1: ['plant', 'tape', 'tissue'],
    2: [],
    3: ['bone'],
    4: ['card'],
    5: [],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'bone'),       # Remove the bone from Box 3
    (0, None, 'document'),   # Remove the document from Box 0
    (0, None, 'engine'),     # Remove the engine from Box 0
    (None, 3, 'bomb'),       # Put the bomb into Box 3
    (3, None, 'bomb'),       # Remove the bomb from Box 3
    (None, 0, 'cheese'),     # Put the cheese into Box 0
    (None, 0, 'milk'),       # Put the milk into Box 0
    (None, 0, 'train'),      # Put the train into Box 0
    (None, 3, 'sheet'),      # Put the sheet into Box 3
    (4, 5, 'card'),          # Move the card from Box 4 to Box 5
    (0, None, 'milk'),       # Remove the milk from Box 0
    (3, None, 'sheet'),      # Remove the sheet from Box 3
    (None, 4, 'clock'),      # Put the clock into Box 4
    (None, 4, 'engine')      # Put the engine into Box 4
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