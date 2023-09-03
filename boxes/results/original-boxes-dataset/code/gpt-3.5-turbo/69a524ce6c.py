# Initialize the boxes
boxes = {
    0: [],
    1: ['bus', 'file'],
    2: ['engine', 'medicine', 'milk'],
    3: ['brain', 'glass'],
    4: ['bomb', 'clock', 'tea'],
    5: ['cream', 'paper', 'wire'],
    6: ['bread', 'cup', 'newspaper'],
}

# Define the moves
moves = [
    (2, None, 'engine'),    # Remove the engine from Box 2
    (2, None, 'medicine'),  # Remove the medicine from Box 2
    (2, None, 'milk'),      # Remove the milk from Box 2
    (None, 1, 'bottle'),    # Put the bottle into Box 1
    (None, 2, 'dress'),     # Put the dress into Box 2
    (6, None, 'bread'),     # Remove the bread from Box 6
    (6, None, 'cup'),       # Remove the cup from Box 6
    (6, None, 'newspaper'), # Remove the newspaper from Box 6
    (3, None, 'brain'),     # Remove the brain from Box 3
    (3, None, 'glass'),     # Remove the glass from Box 3
    (0, None, 'bone'),      # Put the bone into Box 0
    (0, None, 'coat'),      # Put the coat into Box 0
    (4, None, 'clock'),     # Remove the clock from Box 4
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