# Initialize the boxes
boxes = {
    0: ['bomb'],
    1: ['bag', 'bell'],
    2: ['cream', 'drug', 'picture'],
    3: ['letter', 'rose', 'tea'],
    4: ['flower', 'wire'],
    5: ['coffee', 'paper', 'sheet'],
    6: ['cash', 'fig', 'gift'],
}

# Define the moves
moves = [
    (4, None, 'flower'),    # Remove the flower from Box 4
    (4, None, 'wire'),      # Remove the wire from Box 4
    (5, None, 'paper'),     # Remove the paper from Box 5
    (5, None, 'sheet'),     # Remove the sheet from Box 5
    (6, None, 'fig'),       # Remove the fig from Box 6
    (0, None, 'bomb'),      # Remove the bomb from Box 0
    (None, 1, 'tape'),      # Put the tape into Box 1
    (5, 0, 'coffee'),       # Move the coffee from Box 5 to Box 0
    (0, None, 'coffee'),    # Remove the coffee from Box 0
    (2, None, 'picture'),   # Remove the picture from Box 2
    (4, None, 'medicine'),  # Put the medicine into Box 4
    (4, 6, 'medicine'),     # Move the medicine from Box 4 to Box 6
    (2, 5, 'cream'),        # Move the cream from Box 2 to Box 5
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