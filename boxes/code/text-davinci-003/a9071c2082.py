# Initialize the boxes
boxes = {
    0: ['boat', 'shoe', 'television'],
    1: ['camera', 'car', 'plane'],
    2: ['cake'],
    3: ['fan'],
    4: ['cross', 'file', 'note'],
    5: ['chemical'],
    6: [],
}

# Define the moves
moves = [
    (2, 6, 'cake'),         # Move the cake from Box 2 to Box 6
    (None, 5, 'dish'),      # Put the dish into Box 5
    (None, 5, 'stone'),     # Put the stone into Box 5
    (0, 6, 'television'),   # Move the television from Box 0 to Box 6
    (None, 2, 'drink'),     # Put the drink into Box 2
    (5, 2, 'chemical'),     # Move the chemical from Box 5 to Box 2
    (5, 2, 'stone'),        # Move the stone from Box 5 to Box 2
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