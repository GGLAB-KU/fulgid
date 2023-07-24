# Initialize the boxes
boxes = {
    0: [],
    1: ['cigarette'],
    2: ['beer', 'tie'],
    3: [],
    4: ['cream', 'egg', 'knife'],
    5: ['bone'],
    6: ['plate'],
}

# Define the moves
moves = [
    (2, 5, 'tie'),          # Move the tie from Box 2 to Box 5
    (2, 0, 'beer'),         # Move the beer from Box 2 to Box 0
    (6, None, 'plate'),     # Remove the plate from Box 6
    (5, None, 'tie'),       # Remove the tie from Box 5
    (4, None, 'cream'),     # Remove the cream from Box 4
    (None, 5, 'cup'),       # Put the cup into Box 5
    (None, 5, 'drink'),     # Put the drink into Box 5
    (0, 1, 'beer')          # Move the beer from Box 0 to Box 1
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