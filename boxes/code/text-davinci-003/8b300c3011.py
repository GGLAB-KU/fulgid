# Initialize the boxes
boxes = {
    0: ['cigarette'],
    1: ['gift', 'pipe'],
    2: ['camera', 'picture', 'tape'],
    3: ['stone', 'television'],
    4: ['fig', 'key', 'sheet'],
    5: [],
    6: [],
}

# Define the moves
moves = [
    (1, 3, 'gift'),         # Move the gift from Box 1 to Box 3
    (1, None, 'pipe'),      # Remove the pipe from Box 1
    (4, None, 'sheet'),     # Remove the sheet from Box 4
    (0, None, 'cigarette'), # Remove the cigarette from Box 0
    (None, 0, 'ring'),      # Put the ring into Box 0
    (4, None, 'fig'),       # Remove the fig from Box 4
    (4, None, 'key'),       # Remove the key from Box 4
    (1, None, 'cup'),       # Remove the cup from Box 1
    (1, None, 'fig'),       # Remove the fig from Box 1
    (1, None, 'fish'),      # Remove the fish from Box 1
    (0, 4, 'ring'),         # Move the ring from Box 0 to Box 4
    (2, None, 'picture'),   # Remove the picture from Box 2
    (1, None, 'cup'),       # Remove the cup from Box 1
    (1, None, 'fig'),       # Remove the fig from Box 1
    (1, None, 'fish'),      # Remove the fish from Box 1
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