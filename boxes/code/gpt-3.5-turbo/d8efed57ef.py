# Initialize the boxes
boxes = {
    0: [],
    1: ['coat', 'key'],
    2: ['bag'],
    3: [],
    4: ['cash', 'ring'],
    5: ['gift'],
    6: ['television'],
}

# Define the moves
moves = [
    (4, None, 'cash'),       # Remove the cash from Box 4
    (4, None, 'ring'),       # Remove the ring from Box 4
    (1, 4, 'key'),           # Move the key from Box 1 to Box 4
    (1, 5, 'coat'),          # Move the coat from Box 1 to Box 5
    (2, 3, 'bag'),           # Move the bag from Box 2 to Box 3
    (5, None, 'coat'),       # Remove the coat from Box 5
    (5, None, 'gift'),       # Remove the gift from Box 5
    (None, 1, 'apple'),      # Put the apple into Box 1
    (None, 1, 'mirror'),     # Put the mirror into Box 1
    (None, 1, 'plane'),      # Put the plane into Box 1
    (1, 4, 'mirror'),        # Move the mirror from Box 1 to Box 4
    (1, 0, 'apple'),         # Move the apple from Box 1 to Box 0
    (1, 0, 'plane'),         # Move the plane from Box 1 to Box 0
    (0, None, 'apple'),      # Remove the apple from Box 0
    (0, None, 'plane')       # Remove the plane from Box 0
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