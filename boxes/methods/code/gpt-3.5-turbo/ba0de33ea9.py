# Initialize the boxes
boxes = {
    0: ['glass', 'seed', 'sheet'],
    1: ['book'],
    2: [],
    3: ['disk', 'medicine'],
    4: ['magazine'],
    5: ['picture'],
    6: ['card'],
}

# Define the moves
moves = [
    (None, 4, 'crown'),       # Put the crown into Box 4
    (4, 3, 'magazine'),       # Move the magazine from Box 4 to Box 3
    (1, None, 'book'),        # Remove the book from Box 1
    (4, None, 'crown'),       # Remove the crown from Box 4
    (5, 1, 'picture'),        # Move the picture from Box 5 to Box 1
    (0, 2, 'seed'),           # Move the seed from Box 0 to Box 2
    (0, 2, 'sheet'),          # Move the sheet from Box 0 to Box 2
    (6, 2, 'card'),           # Move the card from Box 6 to Box 2
    (2, None, 'seed'),        # Remove the seed from Box 2
    (2, None, 'card'),        # Remove the card from Box 2
    (2, None, 'sheet'),       # Remove the sheet from Box 2
    (1, 0, 'picture'),        # Move the picture from Box 1 to Box 0
    (None, 2, 'document'),    # Put the document into Box 2
    (0, 1, 'glass')           # Move the glass from Box 0 to Box 1
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