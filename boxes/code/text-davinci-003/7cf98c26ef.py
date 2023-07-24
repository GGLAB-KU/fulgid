# Initialize the boxes
boxes = {
    0: ['mirror', 'painting'],
    1: ['file'],
    2: ['cigarette'],
    3: ['rock', 'tissue'],
    4: ['fan'],
    5: [],
    6: ['cash', 'gift'],
}

# Define the moves
moves = [
    (None, 5, 'leaf'),       # Put the leaf into Box 5
    (None, 5, 'machine'),    # Put the machine into Box 5
    (6, None, 'cash'),       # Remove the cash from Box 6
    (6, None, 'gift'),       # Remove the gift from Box 6
    (4, None, 'fan'),        # Remove the fan from Box 4
    (5, None, 'leaf'),       # Remove the leaf from Box 5
    (5, 6, 'machine'),       # Move the machine from Box 5 to Box 6
    (None, 5, 'dish'),       # Put the dish into Box 5
    (None, 5, 'egg'),        # Put the egg into Box 5
    (2, None, 'cigarette'),  # Remove the cigarette from Box 2
    (3, None, 'rock'),       # Remove the rock from Box 3
    (5, 1, 'dish'),          # Move the dish from Box 5 to Box 1
    (0, 6, 'mirror'),        # Move the mirror from Box 0 to Box 6
    (0, 6, 'painting'),      # Move the painting from Box 0 to Box 6
    (1, 5, 'dish'),          # Move the dish from Box 1 to Box 5
    (3, 2, 'tissue'),        # Move the tissue from Box 3 to Box 2
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