# Initialize the boxes
boxes = {
    0: ['cross', 'drug', 'fan'],
    1: ['bag', 'meat', 'tissue'],
    2: ['brick', 'coffee', 'paper'],
    3: ['bread'],
    4: ['bottle', 'radio'],
    5: ['bone', 'drink', 'wheel'],
    6: ['jacket', 'ticket'],
}

# Define the moves
moves = [
    (5, None, 'bone'),       # Remove the bone from Box 5
    (6, 3, 'ticket'),         # Move the ticket from Box 6 to Box 3
    (2, None, 'coffee'),      # Remove the coffee from Box 2
    (2, None, 'paper'),       # Remove the paper from Box 2
    (0, 6, 'drug'),           # Move the drug from Box 0 to Box 6
    (0, 6, 'fan'),            # Move the fan from Box 0 to Box 6
    (None, 5, 'computer'),    # Put the computer into Box 5
    (2, None, 'brick'),       # Remove the brick from Box 2
    (2, 3, 'brick'),          # Put the brick into Box 3
    (None, 4, 'tie'),         # Put the tie into Box 4
    (4, 0, 'bottle'),         # Move the bottle from Box 4 to Box 0
    (5, None, 'computer'),    # Remove the computer from Box 5
    (5, None, 'drink')        # Remove the drink from Box 5
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