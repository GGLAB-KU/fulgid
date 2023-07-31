# Initialize the boxes
boxes = {
    0: [],
    1: ['disk', 'drink', 'fig'],
    2: [],
    3: ['block', 'shirt'],
    4: ['bus', 'key', 'rose'],
    5: ['crown', 'painting', 'wheel'],
    6: ['boot', 'cigarette'],
}

# Define the moves
moves = [
    (5, 2, 'crown'),        # Move the crown from Box 5 to Box 2
    (5, 2, 'wheel'),        # Move the wheel from Box 5 to Box 2
    (None, 2, 'letter'),    # Put the letter into Box 2
    (5, None, 'painting'),  # Remove the painting from Box 5
    (1, 0, 'disk'),         # Move the disk from Box 1 to Box 0
    (0, None, 'disk'),      # Remove the disk from Box 0
    (6, None, 'boot'),      # Remove the boot from Box 6
    (6, None, 'cigarette'), # Remove the cigarette from Box 6
    (2, None, 'letter'),    # Remove the letter from Box 2
    (2, None, 'wheel'),     # Remove the wheel from Box 2
    (3, None, 'block'),     # Remove the block from Box 3
    (4, None, 'bus'),       # Remove the bus from Box 4
    (None, 4, 'ice'),       # Put the ice into Box 4
    (3, None, 'shirt'),     # Remove the shirt from Box 3
    (None, 2, 'wheel'),     # Put the wheel into Box 2
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