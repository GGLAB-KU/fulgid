# Initialize the boxes
boxes = {
    0: ['bus', 'glass', 'television'],
    1: [],
    2: ['flower', 'phone', 'wheel'],
    3: ['medicine', 'train'],
    4: ['chemical', 'disk'],
    5: ['cash', 'game', 'shell'],
    6: [],
}

# Define the moves
moves = [
    (None, 3, 'ring'),          # Put the ring into Box 3
    (None, 1, 'cigarette'),     # Put the cigarette into Box 1
    (1, 6, 'cigarette'),        # Move the cigarette from Box 1 to Box 6
    (2, None, 'flower'),        # Remove the flower from Box 2
    (2, None, 'phone'),         # Remove the phone from Box 2
    (6, None, 'cigarette'),     # Remove the cigarette from Box 6
    (2, None, 'wheel'),         # Remove the wheel from Box 2
    (5, None, 'game'),          # Remove the game from Box 5
    (0, 6, 'bus'),              # Move the bus from Box 0 to Box 6
    (None, 2, 'block'),         # Put the block into Box 2
    (None, 2, 'cheese'),        # Put the cheese into Box 2
    (3, 6, 'ring'),             # Move the ring from Box 3 to Box 6
    (3, 6, 'train')             # Move the train from Box 3 to Box 6
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