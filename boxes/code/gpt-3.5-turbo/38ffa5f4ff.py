# Initialize the boxes
boxes = {
    0: ['brain'],
    1: ['radio'],
    2: ['boat', 'tie'],
    3: ['bomb', 'tea'],
    4: ['bone', 'note', 'stone'],
    5: ['apple', 'dress', 'paper'],
    6: ['branch', 'guitar', 'shell'],
}

# Define the moves
moves = [
    (6, None, 'branch'),       # Remove the branch from Box 6
    (1, None, 'radio'),        # Remove the radio from Box 1
    (4, 1, 'bone'),            # Move the bone from Box 4 to Box 1
    (4, 1, 'stone'),           # Move the stone from Box 4 to Box 1
    (3, None, 'tea'),          # Remove the tea from Box 3
    (1, None, 'bone'),         # Remove the bone from Box 1
    (1, None, 'stone'),        # Remove the stone from Box 1
    (0, None, 'brain'),        # Remove the brain from Box 0
    (2, None, 'boat'),         # Remove the boat from Box 2
    (2, 1, 'tie'),             # Move the tie from Box 2 to Box 1
    (5, 2, 'apple'),           # Move the apple from Box 5 to Box 2
    (5, 2, 'dress'),           # Move the dress from Box 5 to Box 2
    (2, None, 'apple'),        # Remove the apple from Box 2
    (5, 0, 'paper'),           # Move the paper from Box 5 to Box 0
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