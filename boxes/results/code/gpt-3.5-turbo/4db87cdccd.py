# Initialize the boxes
boxes = {
    0: ['disk', 'jacket', 'seed'],
    1: ['clock', 'cream', 'phone'],
    2: ['brain', 'dish', 'radio'],
    3: ['document', 'game'],
    4: ['bag', 'engine', 'train'],
    5: ['shell'],
    6: ['egg'],
}

# Define the moves
moves = [
    (1, None, 'cream'),     # Remove the cream from Box 1
    (5, None, 'shell'),     # Remove the shell from Box 5
    (0, None, 'disk'),      # Remove the disk from Box 0
    (0, None, 'jacket'),    # Remove the jacket from Box 0
    (0, None, 'seed'),      # Remove the seed from Box 0
    (None, 1, 'cross'),     # Put the cross into Box 1
    (4, None, 'bag'),       # Remove the bag from Box 4
    (None, 5, 'fish'),      # Put the fish into Box 5
    (4, None, 'engine'),    # Remove the engine from Box 4
    (4, None, 'train'),     # Remove the train from Box 4
    (2, None, 'brain'),     # Remove the brain from Box 2
    (None, 4, 'boat'),      # Put the boat into Box 4
    (None, 4, 'plant')      # Put the plant into Box 4
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