# Initialize the boxes
boxes = {
    0: ['bag'],
    1: ['drug', 'wire'],
    2: ['branch', 'leaf', 'ticket'],
    3: ['coffee', 'milk', 'plane'],
    4: [],
    5: [],
    6: ['television'],
}

# Define the moves
moves = [
    (1, 6, 'wire'),         # Move the wire from Box 1 to Box 6
    (6, None, 'wire'),      # Remove the wire from Box 6
    (2, None, 'branch'),    # Remove the branch from Box 2
    (3, None, 'plane'),     # Remove the plane from Box 3
    (1, None, 'drug'),      # Remove the drug from Box 1
    (2, 6, 'ticket'),       # Move the ticket from Box 2 to Box 6
    (6, 1, 'television'),   # Move the television from Box 6 to Box 1
    (2, None, 'ticket'),    # Remove the ticket from Box 2
    (3, None, 'coffee'),    # Remove the coffee from Box 3
    (3, None, 'milk'),      # Remove the milk from Box 3
    (None, 1, 'shoe'),      # Put the shoe into Box 1
    (1, 0, 'shoe'),         # Move the shoe from Box 1 to Box 0
    (2, 0, 'leaf')          # Move the leaf from Box 2 to Box 0
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