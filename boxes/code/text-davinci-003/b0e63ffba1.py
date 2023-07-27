# Initialize the boxes
boxes = {
    0: ['ball', 'cheese', 'key'],
    1: ['paper'],
    2: ['fig', 'knife', 'rose'],
    3: ['file', 'fish', 'rock'],
    4: ['picture'],
    5: ['book', 'car', 'medicine'],
    6: ['sheet'],
}

# Define the moves
moves = [
    (3, None, 'file'),       # Remove the file from Box 3
    (0, None, 'key'),        # Remove the key from Box 0
    (0, 3, 'ball'),          # Move the ball from Box 0 to Box 3
    (3, None, 'ball'),       # Remove the ball from Box 3
    (3, None, 'fish'),       # Remove the fish from Box 3
    (6, None, 'sheet'),      # Remove the sheet from Box 6
    (1, 3, 'paper'),         # Move the paper from Box 1 to Box 3
    (4, None, 'picture'),    # Remove the picture from Box 4
    (0, None, 'cheese'),     # Remove the cheese from Box 0
    (2, 1, 'fig'),           # Move the fig from Box 2 to Box 1
    (5, 4, 'car'),           # Move the car from Box 5 to Box 4
    (5, 4, 'medicine'),      # Move the medicine from Box 5 to Box 4
    (1, None, 'fig'),        # Remove the fig from Box 1
    (None, 3, 'engine')      # Put the engine into Box 3
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