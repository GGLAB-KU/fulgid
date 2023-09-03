# Initialize the boxes
boxes = {
    0: ['computer', 'disk'],
    1: ['bone', 'dress', 'fan'],
    2: ['string', 'train'],
    3: ['meat'],
    4: ['boat'],
    5: ['cake', 'gift'],
    6: ['creature', 'knife', 'milk'],
}

# Define the moves
moves = [
    (5, None, 'cake'),       # Remove the cake from Box 5
    (5, 0, 'gift'),          # Move the gift from Box 5 to Box 0
    (None, 4, 'shirt'),      # Put the shirt into Box 4
    (4, None, 'shirt'),      # Remove the shirt from Box 4
    (0, None, 'gift'),       # Remove the gift from Box 0
    (None, 3, 'chemical'),   # Put the chemical into Box 3
    (2, 5, 'string'),        # Move the string from Box 2 to Box 5
    (2, 5, 'train'),         # Move the train from Box 2 to Box 5
    (1, None, 'dress'),      # Remove the dress from Box 1
    (1, None, 'fan'),        # Remove the fan from Box 1
    (5, None, 'train'),      # Remove the train from Box 5
    (4, None, 'boat'),       # Remove the boat from Box 4
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