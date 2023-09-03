# Initialize the boxes
boxes = {
    0: ['car', 'coat', 'flower'],
    1: ['document', 'leaf'],
    2: ['picture', 'pot'],
    3: ['file', 'medicine'],
    4: ['cheese', 'radio', 'ring'],
    5: ['bottle', 'seed', 'sheet'],
    6: [],
}

# Define the moves
moves = [
    (None, 1, 'drink'),     # Put the drink into Box 1
    (5, None, 'sheet'),     # Remove the sheet from Box 5
    (0, None, 'coat'),      # Remove the coat from Box 0
    (None, 3, 'dress'),     # Put the dress into Box 3
    (3, 6, 'dress'),        # Move the dress from Box 3 to Box 6
    (3, 6, 'file'),         # Move the file from Box 3 to Box 6
    (3, None, 'medicine'),  # Remove the medicine from Box 3
    (None, 5, 'ball'),      # Put the ball into Box 5
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