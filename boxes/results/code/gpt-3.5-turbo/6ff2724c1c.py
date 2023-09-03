# Initialize the boxes
boxes = {
    0: ['egg'],
    1: ['ticket'],
    2: ['car', 'gift', 'shoe'],
    3: ['document', 'suit'],
    4: ['computer', 'crown'],
    5: ['knife', 'pot', 'shell'],
    6: ['branch', 'machine', 'tea'],
}

# Define the moves
moves = [
    (4, None, 'crown'),       # Remove the crown from Box 4
    (0, 3, 'egg'),            # Move the egg from Box 0 to Box 3
    (6, 0, 'machine'),        # Move the machine from Box 6 to Box 0
    (2, None, 'car'),         # Remove the car from Box 2
    (2, None, 'shoe'),        # Remove the shoe from Box 2
    (3, 2, 'document'),       # Move the document from Box 3 to Box 2
    (3, 2, 'suit'),           # Move the suit from Box 3 to Box 2
    (1, None, 'ticket'),      # Remove the ticket from Box 1
    (4, None, 'computer'),    # Remove the computer from Box 4
    (3, None, 'egg')          # Remove the egg from Box 3
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