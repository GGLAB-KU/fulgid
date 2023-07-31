# Initialize the boxes
boxes = {
    0: ['string'],
    1: ['bus', 'flower', 'leaf'],
    2: [],
    3: ['bell'],
    4: ['camera', 'picture'],
    5: ['ball', 'book', 'drink'],
    6: [],
}

# Define the moves
moves = [
    (5, None, 'ball'),       # Remove the ball from Box 5
    (0, None, 'string'),     # Remove the string from Box 0
    (None, 0, 'ticket'),     # Put the ticket into Box 0
    (None, 5, 'dress'),      # Put the dress into Box 5
    (5, None, 'book'),       # Remove the book from Box 5
    (5, None, 'drink'),      # Remove the drink from Box 5
    (1, 0, 'bus'),           # Move the bus from Box 1 to Box 0
    (None, 2, 'jacket'),     # Put the jacket into Box 2
    (None, 0, 'meat'),       # Put the meat into Box 0
    (0, 6, 'meat'),          # Move the meat from Box 0 to Box 6
    (1, 3, 'flower'),        # Move the flower from Box 1 to Box 3
    (1, 3, 'leaf'),          # Move the leaf from Box 1 to Box 3
    (0, None, 'ticket'),     # Remove the ticket from Box 0
    (4, 2, 'camera'),        # Move the camera from Box 4 to Box 2
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