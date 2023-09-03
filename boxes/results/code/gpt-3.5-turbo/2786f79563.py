# Initialize the boxes
boxes = {
    0: ['bread', 'letter', 'ticket'],
    1: ['cash', 'paper', 'string'],
    2: ['bowl', 'fig', 'plate'],
    3: ['block', 'tea'],
    4: ['brick', 'gift'],
    5: ['engine', 'flower', 'milk'],
    6: [],
}

# Define the moves
moves = [
    (0, None, 'bread'),     # Remove the bread from Box 0
    (0, None, 'letter'),    # Remove the letter from Box 0
    (0, None, 'ticket'),    # Remove the ticket from Box 0
    (1, None, 'cash'),      # Remove the cash from Box 1
    (1, None, 'paper'),     # Remove the paper from Box 1
    (1, None, 'string'),    # Remove the string from Box 1
    (2, None, 'bowl'),      # Remove the bowl from Box 2
    (2, None, 'fig'),       # Remove the fig from Box 2
    (2, None, 'plate'),     # Remove the plate from Box 2
    (3, None, 'block'),     # Remove the block from Box 3
    (3, None, 'tea'),       # Remove the tea from Box 3
    (4, None, 'brick'),     # Remove the brick from Box 4
    (4, None, 'gift'),      # Remove the gift from Box 4
    (5, None, 'engine'),    # Remove the engine from Box 5
    (5, None, 'flower'),    # Remove the flower from Box 5
    (5, None, 'milk'),      # Remove the milk from Box 5
    (None, 6, 'block'),     # Move the block to Box 6
    (None, 6, 'tea'),       # Move the tea to Box 6
    (None, 6, 'brick'),     # Move the brick to Box 6
    (None, 6, 'gift'),      # Move the gift to Box 6
    (None, 6, 'engine'),    # Move the engine to Box 6
    (None, 6, 'flower'),    # Move the flower to Box 6
    (None, 6, 'milk'),      # Move the milk to Box 6
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