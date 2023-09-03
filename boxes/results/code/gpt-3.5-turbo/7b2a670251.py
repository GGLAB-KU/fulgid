# Initialize the boxes
boxes = {
    0: ['card', 'clock'],
    1: ['camera', 'cash', 'computer'],
    2: ['bottle', 'chemical', 'key'],
    3: [],
    4: ['creature', 'document'],
    5: ['car', 'coffee'],
    6: ['bomb', 'leaf', 'tie'],
}

# Define the moves
moves = [
    (2, 5, 'bottle'),       # Move the bottle from Box 2 to Box 5
    (5, 4, 'coffee'),       # Move the coffee from Box 5 to Box 4
    (1, None, 'computer'),  # Remove the computer from Box 1
    (1, None, 'camera'),    # Remove the camera from Box 1
    (1, None, 'cash'),      # Remove the cash from Box 1
    (6, None, 'bomb'),      # Remove the bomb from Box 6
    (6, None, 'tie'),       # Remove the tie from Box 6
    (5, 6, 'bottle'),       # Move the bottle from Box 5 to Box 6
    (5, 6, 'car'),          # Move the car from Box 5 to Box 6
    (None, 1, 'meat'),      # Put the meat into Box 1
    (None, 1, 'painting'),  # Put the painting into Box 1
    (4, None, 'coffee'),    # Remove the coffee from Box 4
    (4, 5, 'creature'),     # Move the creature from Box 4 to Box 5
    (4, 5, 'document'),     # Move the document from Box 4 to Box 5
    (0, None, 'clock'),     # Remove the clock from Box 0
    (0, 5, 'card'),         # Move the card from Box 0 to Box 5
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