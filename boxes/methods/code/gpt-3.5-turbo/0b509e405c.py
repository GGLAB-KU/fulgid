# Initialize the boxes
boxes = {
    0: [],
    1: ['coat', 'drug'],
    2: [],
    3: [],
    4: [],
    5: ['computer', 'cross', 'pipe'],
    6: ['glass'],
}

# Define the moves
moves = [
    (5, None, 'computer'),  # Remove the computer from Box 5
    (5, None, 'cross'),     # Remove the cross from Box 5
    (None, 5, 'bread'),     # Put the bread into Box 5
    (None, 5, 'milk'),      # Put the milk into Box 5
    (6, None, 'glass'),     # Remove the glass from Box 6
    (1, 2, 'coat'),         # Move the coat from Box 1 to Box 2
    (1, 2, 'drug'),         # Move the drug from Box 1 to Box 2
    (None, 3, 'bone'),      # Put the bone into Box 3
    (None, 3, 'file'),      # Put the file into Box 3
    (None, 4, 'apple'),     # Put the apple into Box 4
    (4, None, 'apple'),     # Remove the apple from Box 4
    (3, 2, 'file'),         # Move the file from Box 3 to Box 2
    (6, 3, 'glass'),        # Put the glass into Box 3
    (3, 6, 'bone'),         # Move the bone from Box 3 to Box 6
    (1, 3, 'glass'),        # Move the glass from Box 1 to Box 3
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