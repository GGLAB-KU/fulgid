# Initialize the boxes
boxes = {
    0: ['fig', 'suit'],
    1: ['creature'],
    2: ['clock'],
    3: ['cake', 'dish'],
    4: ['drug', 'letter', 'plane'],
    5: ['cross', 'tissue'],
    6: ['block', 'game', 'radio'],
}

# Define the moves
moves = [
    (4, None, 'letter'),    # Remove the letter from Box 4
    (6, None, 'game'),      # Remove the game from Box 6
    (2, None, 'clock'),     # Remove the clock from Box 2
    (None, 4, 'dress'),     # Put the dress into Box 4
    (4, None, 'dress'),     # Remove the dress from Box 4
    (4, None, 'drug'),      # Remove the drug from Box 4
    (4, None, 'plane'),     # Remove the plane from Box 4
    (None, 1, 'dress'),     # Put the dress into Box 1
    (None, 1, 'engine'),    # Put the engine into Box 1
    (6, 0, 'block'),        # Move the block from Box 6 to Box 0
    (5, None, 'cross'),     # Remove the cross from Box 5
    (5, None, 'tissue'),    # Remove the tissue from Box 5
    (3, 5, 'cake'),         # Move the cake from Box 3 to Box 5
    (3, None, 'dish'),      # Remove the dish from Box 3
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