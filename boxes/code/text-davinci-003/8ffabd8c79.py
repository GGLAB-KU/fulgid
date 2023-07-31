# Initialize the boxes
boxes = {
    0: ['book', 'fan', 'radio'],
    1: ['bus', 'crown', 'suit'],
    2: ['leaf', 'shell', 'stone'],
    3: ['apple', 'hat', 'plane'],
    4: ['brain', 'card', 'cigarette'],
    5: ['seed'],
    6: ['disk', 'painting', 'sheet'],
}

# Define the moves
moves = [
    (0, None, 'fan'),       # Remove the fan from Box 0
    (3, None, 'plane'),     # Remove the plane from Box 3
    (2, None, 'leaf'),      # Remove the leaf from Box 2
    (2, None, 'stone'),     # Remove the stone from Box 2
    (4, None, 'cigarette'), # Remove the cigarette from Box 4
    (4, 2, 'brain'),        # Move the brain from Box 4 to Box 2
    (4, 2, 'card'),         # Move the card from Box 4 to Box 2
    (5, None, 'seed'),      # Remove the seed from Box 5
    (None, 4, 'bowl'),      # Put the bowl into Box 4
    (None, 4, 'pot'),       # Put the pot into Box 4
    (3, None, 'apple'),     # Remove the apple from Box 3
    (1, None, 'crown'),     # Remove the crown from Box 1
    (2, 3, 'brain'),        # Move the brain from Box 2 to Box 3
    (2, 3, 'card'),         # Move the card from Box 2 to Box 3
    (4, None, 'bowl'),      # Remove the bowl from Box 4
    (1, None, 'suit'),      # Remove the suit from Box 1
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