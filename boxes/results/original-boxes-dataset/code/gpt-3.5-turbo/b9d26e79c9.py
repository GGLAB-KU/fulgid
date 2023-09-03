# Initialize the boxes
boxes = {
    0: ['bag'],
    1: ['coffee', 'tape'],
    2: ['cheese', 'drug', 'picture'],
    3: [],
    4: ['drink', 'note'],
    5: ['ball'],
    6: ['machine', 'tie'],
}

# Define the moves
moves = [
    (0, None, 'bag'),       # Remove the bag from Box 0
    (None, 6, 'ice'),       # Put the ice into Box 6
    (None, 0, 'bag'),       # Put the bag into Box 0
    (None, 0, 'plant'),     # Put the plant into Box 0
    (2, 3, 'cheese'),       # Move the cheese from Box 2 to Box 3
    (2, 3, 'picture'),      # Move the picture from Box 2 to Box 3
    (6, None, 'machine'),   # Remove the machine from Box 6
    (4, None, 'note'),      # Remove the note from Box 4
    (6, 0, 'ice'),          # Move the ice from Box 6 to Box 0
    (2, 6, 'drug'),         # Move the drug from Box 2 to Box 6
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