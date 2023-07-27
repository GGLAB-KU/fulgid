# Initialize the boxes
boxes = {
    0: [],
    1: ['bomb', 'cup'],
    2: ['clock', 'jacket', 'wire'],
    3: ['picture'],
    4: [],
    5: ['chemical', 'medicine', 'rock'],
    6: ['pipe'],
}

# Define the moves
moves = [
    (None, 0, 'drug'),       # Put the drug into Box 0
    (1, None, 'bomb'),       # Remove the bomb from Box 1
    (5, None, 'chemical'),   # Remove the chemical from Box 5
    (5, None, 'rock'),       # Remove the rock from Box 5
    (None, 5, 'train'),      # Put the train into Box 5
    (None, 5, 'watch'),      # Put the watch into Box 5
    (5, None, 'medicine'),   # Remove the medicine from Box 5
    (5, None, 'train'),      # Remove the train from Box 5
    (6, None, 'string'),     # Put the string into Box 6
    (None, 0, 'ball'),       # Put the ball into Box 0
    (None, 0, 'egg'),        # Put the egg into Box 0
    (6, 5, 'pipe'),          # Move the pipe from Box 6 to Box 5
    (6, 5, 'string')         # Move the string from Box 6 to Box 5
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