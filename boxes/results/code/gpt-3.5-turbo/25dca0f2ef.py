# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['document', 'flower', 'machine'],
    3: ['cream'],
    4: ['bone'],
    5: ['knife', 'pot'],
    6: ['phone', 'rock'],
}

# Define the moves
moves = [
    (4, None, 'bone'),       # Remove the bone from Box 4
    (5, 6, 'pot'),           # Move the pot from Box 5 to Box 6
    (6, 1, 'rock'),          # Move the rock from Box 6 to Box 1
    (1, 0, 'rock'),          # Move the rock from Box 1 to Box 0
    (2, None, 'document'),   # Remove the document from Box 2
    (2, None, 'machine'),    # Remove the machine from Box 2
    (2, 1, 'flower'),        # Move the flower from Box 2 to Box 1
    (None, 1, 'milk'),       # Put the milk into Box 1
    (None, 1, 'tea'),        # Put the tea into Box 1
    (6, None, 'phone'),      # Remove the phone from Box 6
    (6, None, 'pot'),        # Remove the pot from Box 6
    (5, None, 'knife'),      # Remove the knife from Box 5
    (None, 5, 'shoe'),       # Put the shoe into Box 5
    (None, 4, 'book'),       # Put the book into Box 4
    (None, 4, 'pipe'),       # Put the pipe into Box 4
    (None, 4, 'sheet')       # Put the sheet into Box 4
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