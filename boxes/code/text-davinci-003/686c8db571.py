# Initialize the boxes
boxes = {
    0: [],
    1: ['string'],
    2: ['shirt'],
    3: ['coffee', 'file', 'wire'],
    4: ['cash', 'suit', 'tape'],
    5: ['brick', 'radio', 'tea'],
    6: ['paper'],
}

# Define the moves
moves = [
    (4, None, 'cash'),       # Remove the cash from Box 4
    (4, None, 'suit'),       # Remove the suit from Box 4
    (4, None, 'tape'),       # Remove the tape from Box 4
    (1, None, 'string'),     # Remove the string from Box 1
    (5, None, 'brick'),      # Remove the brick from Box 5
    (5, None, 'radio'),      # Remove the radio from Box 5
    (5, None, 'tea'),        # Remove the tea from Box 5
    (None, 0, 'brick'),      # Put the brick into Box 0
    (None, 5, 'document'),   # Put the document into Box 5
    (None, 5, 'note'),       # Put the note into Box 5
    (None, 5, 'train'),      # Put the train into Box 5
    (2, None, 'shirt'),      # Remove the shirt from Box 2
    (3, 2, 'coffee'),        # Move the coffee from Box 3 to Box 2
    (3, 2, 'file'),          # Move the file from Box 3 to Box 2
    (3, None, 'wire'),       # Remove the wire from Box 3
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