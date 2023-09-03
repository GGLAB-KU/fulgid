# Initialize the boxes
boxes = {
    0: ['block', 'cheese', 'train'],
    1: ['apple'],
    2: ['dress', 'milk'],
    3: ['ice', 'plant'],
    4: ['car', 'seed', 'tape'],
    5: ['bus', 'egg'],
    6: [],
}

# Define the moves
moves = [
    (5, None, 'bus'),       # Remove the bus from Box 5
    (1, None, 'apple'),     # Remove the apple from Box 1
    (4, 3, 'car'),          # Move the car from Box 4 to Box 3
    (3, None, 'car'),       # Remove the car from Box 3
    (3, None, 'ice'),       # Remove the ice from Box 3
    (4, None, 'tape'),      # Remove the tape from Box 4
    (3, 1, 'plant'),        # Move the plant from Box 3 to Box 1
    (4, 2, 'seed'),         # Move the seed from Box 4 to Box 2
    (2, 6, 'dress'),        # Move the dress from Box 2 to Box 6
    (2, 6, 'milk'),         # Move the milk from Box 2 to Box 6
    (2, None, 'seed'),      # Remove the seed from Box 2
    (None, 5, 'stone'),     # Put the stone into Box 5
    (0, 3, 'block'),        # Move the block from Box 0 to Box 3
    (3, 1, 'block'),        # Move the block from Box 3 to Box 1
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