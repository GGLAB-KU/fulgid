# Initialize the boxes
boxes = {
    0: [],
    1: ['guitar', 'picture', 'suit'],
    2: ['cake', 'pot', 'sheet'],
    3: ['computer'],
    4: ['card', 'meat', 'plant'],
    5: ['newspaper', 'radio', 'wheel'],
    6: ['engine', 'letter'],
}

# Define the moves
moves = [
    (2, None, 'sheet'),       # Remove the sheet from Box 2
    (2, None, 'pot'),         # Remove the pot from Box 2
    (3, None, 'computer'),    # Remove the computer from Box 3
    (None, 3, 'television'),   # Put the television into Box 3
    (5, None, 'newspaper'),   # Remove the newspaper from Box 5
    (5, None, 'wheel'),       # Remove the wheel from Box 5
    (2, 5, 'cake'),           # Move the cake from Box 2 to Box 5
    (1, None, 'guitar'),      # Remove the guitar from Box 1
    (6, 3, 'engine'),         # Move the engine from Box 6 to Box 3
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