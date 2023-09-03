# Initialize the boxes
boxes = {
    0: ['tissue'],
    1: ['document', 'fig', 'wheel'],
    2: ['brick', 'camera', 'cream'],
    3: [],
    4: ['flower', 'glass', 'milk'],
    5: ['boot', 'coffee'],
    6: ['cup', 'paper'],
}

# Define the moves
moves = [
    (1, None, 'document'),   # Remove the document from Box 1
    (1, None, 'fig'),        # Remove the fig from Box 1
    (4, None, 'milk'),       # Remove the milk from Box 4
    (6, None, 'cup'),        # Remove the cup from Box 6
    (6, None, 'paper'),      # Remove the paper from Box 6
    (1, 3, 'wheel'),         # Move the wheel from Box 1 to Box 3
    (None, 1, 'engine'),     # Put the engine into Box 1
    (None, 1, 'ring'),       # Put the ring into Box 1
    (0, 5, 'tissue'),        # Move the tissue from Box 0 to Box 5
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