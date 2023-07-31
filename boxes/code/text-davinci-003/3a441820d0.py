# Initialize the boxes
boxes = {
    0: ['computer', 'ring'],
    1: ['card', 'key', 'shirt'],
    2: ['brick', 'dish', 'medicine'],
    3: ['pipe'],
    4: ['newspaper'],
    5: ['bone', 'paper'],
    6: ['ticket'],
}

# Define the moves
moves = [
    (6, None, 'ticket'),     # Remove the ticket from Box 6
    (4, None, 'newspaper'),  # Remove the newspaper from Box 4
    (None, 6, 'fish'),       # Put the fish into Box 6
    (None, 6, 'gift'),       # Put the gift into Box 6
    (None, 6, 'tape'),       # Put the tape into Box 6
    (None, 5, 'drink'),      # Put the drink into Box 5
    (3, None, 'pipe'),       # Remove the pipe from Box 3
    (2, 4, 'brick'),         # Move the brick from Box 2 to Box 4
    (None, 4, 'meat'),       # Put the meat into Box 4
    (None, 4, 'mirror'),     # Put the mirror into Box 4
    (4, None, 'meat'),       # Remove the meat from Box 4
    (4, None, 'mirror'),     # Remove the mirror from Box 4
    (5, None, 'bone'),       # Remove the bone from Box 5
    (5, None, 'paper'),      # Remove the paper from Box 5
    (1, 2, 'key'),           # Move the key from Box 1 to Box 2
    (2, None, 'dish'),       # Remove the dish from Box 2
    (2, None, 'key'),        # Remove the key from Box 2
    (5, None, 'drink')       # Remove the drink from Box 5
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