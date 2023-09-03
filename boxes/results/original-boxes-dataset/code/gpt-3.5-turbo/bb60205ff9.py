# Initialize the boxes
boxes = {
    0: ['brick'],
    1: ['bag', 'boat', 'coffee'],
    2: ['boot', 'cigarette', 'watch'],
    3: ['card', 'engine', 'milk'],
    4: ['computer', 'drug', 'seed'],
    5: ['ball', 'bottle', 'pot'],
    6: ['map', 'wire'],
}

# Define the moves
moves = [
    (3, 6, 'card'),         # Move the card from Box 3 to Box 6
    (4, None, 'drug'),      # Remove the drug from Box 4
    (4, None, 'seed'),      # Remove the seed from Box 4
    (3, None, 'engine'),    # Remove the engine from Box 3
    (3, None, 'milk'),      # Remove the milk from Box 3
    (2, 4, 'watch'),        # Move the watch from Box 2 to Box 4
    (None, 3, 'block'),     # Put the block into Box 3
    (None, 0, 'dress'),     # Put the dress into Box 0
    (None, 0, 'jacket'),    # Put the jacket into Box 0
    (1, None, 'bag'),       # Remove the bag from Box 1
    (1, None, 'coffee'),    # Remove the coffee from Box 1
    (3, 2, 'block'),        # Move the block from Box 3 to Box 2
    (5, None, 'bottle'),    # Remove the bottle from Box 5
    (None, 5, 'machine'),   # Put the machine into Box 5
    (None, 3, 'pipe'),      # Put the pipe into Box 3
    (0, None, 'brick'),     # Remove the brick from Box 0
    (0, None, 'jacket')     # Remove the jacket from Box 0
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