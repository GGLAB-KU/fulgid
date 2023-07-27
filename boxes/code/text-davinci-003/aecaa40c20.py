# Initialize the boxes
boxes = {
    0: ['note'],
    1: ['plate', 'tea'],
    2: ['document'],
    3: ['branch', 'cross'],
    4: ['coffee', 'drug'],
    5: ['newspaper'],
    6: ['flower', 'sheet'],
}

# Define the moves
moves = [
    (2, None, 'picture'),    # Put the picture into Box 2
    (2, None, 'ticket'),     # Put the ticket into Box 2
    (0, 6, 'note'),          # Move the note from Box 0 to Box 6
    (None, 1, 'key'),        # Put the key into Box 1
    (1, 5, 'tea'),           # Move the tea from Box 1 to Box 5
    (None, 5, 'disk'),       # Put the disk into Box 5
    (1, 0, 'key'),           # Move the key from Box 1 to Box 0
    (1, 0, 'plate'),         # Move the plate from Box 1 to Box 0
    (2, None, 'ticket'),     # Remove the ticket from Box 2
    (4, None, 'coffee'),     # Remove the coffee from Box 4
    (4, None, 'drug'),       # Remove the drug from Box 4
    (3, None, 'branch'),     # Remove the branch from Box 3
    (3, None, 'cross'),      # Remove the cross from Box 3
    (None, 2, 'letter'),     # Put the letter into Box 2
    (2, 3, 'letter'),        # Move the letter from Box 2 to Box 3
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