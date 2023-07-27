# Initialize the boxes
boxes = {
    0: [],
    1: ['medicine'],
    2: ['bomb', 'brick'],
    3: ['cigarette'],
    4: ['paper'],
    5: ['newspaper'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'cigarette'),     # Remove the cigarette from Box 3
    (4, 1, 'paper'),            # Move the paper from Box 4 to Box 1
    (None, 3, 'block'),         # Put the block into Box 3
    (None, 3, 'dress'),         # Put the dress into Box 3
    (None, 3, 'ticket'),        # Put the ticket into Box 3
    (5, None, 'newspaper'),     # Remove the newspaper from Box 5
    (3, None, 'dress')          # Remove the dress from Box 3
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