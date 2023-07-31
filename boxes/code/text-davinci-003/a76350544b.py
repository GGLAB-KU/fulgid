# Initialize the boxes
boxes = {
    0: ['branch', 'drug'],
    1: ['gift', 'seed'],
    2: ['crown'],
    3: ['brain', 'suit'],
    4: ['watch'],
    5: ['book', 'pot', 'shell'],
    6: ['coat', 'dish'],
}

# Define the moves
moves = [
    (None, 4, 'jacket'),    # Put the jacket into Box 4
    (0, None, 'branch'),    # Remove the branch from Box 0
    (0, None, 'drug'),      # Remove the drug from Box 0
    (4, None, 'jacket'),    # Remove the jacket from Box 4
    (1, None, 'gift'),      # Remove the gift from Box 1
    (4, None, 'watch'),     # Remove the watch from Box 4
    (None, 6, 'dress'),     # Put the dress into Box 6
    (5, 4, 'shell'),        # Move the shell from Box 5 to Box 4
    (4, 3, 'shell'),        # Move the shell from Box 4 to Box 3
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