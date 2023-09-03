# Initialize the boxes
boxes = {
    0: ['knife'],
    1: ['ball', 'cigarette', 'coat'],
    2: ['card', 'fig', 'ring'],
    3: ['bag', 'camera', 'gift'],
    4: ['clock', 'tie'],
    5: [],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'card'),       # Remove the card from Box 2
    (2, None, 'fig'),        # Remove the fig from Box 2
    (4, 2, 'clock'),         # Move the clock from Box 4 to Box 2
    (1, 6, 'coat'),          # Move the coat from Box 1 to Box 6
    (4, None, 'tie'),        # Remove the tie from Box 4
    (0, 4, 'knife'),         # Move the knife from Box 0 to Box 4
    (4, None, 'knife'),      # Remove the knife from Box 4
    (None, 1, 'knife'),      # Put the knife into Box 1
    (None, 5, 'car'),        # Put the car into Box 5
    (None, 5, 'pot'),        # Put the pot into Box 5
    (1, 4, 'cigarette'),     # Move the cigarette from Box 1 to Box 4
    (4, None, 'cigarette'),  # Remove the cigarette from Box 4
    (3, None, 'bag'),        # Remove the bag from Box 3
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