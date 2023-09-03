# Initialize the boxes
boxes = {
    0: ['bone', 'television'],
    1: ['drink', 'fig'],
    2: ['glass'],
    3: ['pot'],
    4: ['key', 'plate', 'shoe'],
    5: ['beer', 'egg'],
    6: [],
}

# Define the moves
moves = [
    (3, 2, 'pot'),       # Move the pot from Box 3 to Box 2
    (None, 1, 'gift'),   # Put the gift into Box 1
    (0, None, 'bone'),   # Remove the bone from Box 0
    (1, 2, 'drink'),     # Move the drink from Box 1 to Box 2
    (None, 6, 'cream'),  # Put the cream into Box 6
    (2, None, 'drink'),  # Remove the drink from Box 2
    (2, None, 'pot'),    # Remove the pot from Box 2
    (1, None, 'gift'),   # Remove the gift from Box 1
    (0, None, 'television'),  # Remove the television from Box 0
    (2, 5, 'glass'),     # Move the glass from Box 2 to Box 5
    (None, 3, 'game'),   # Put the game into Box 3
    (1, None, 'fig'),    # Remove the fig from Box 1
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