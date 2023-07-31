# Initialize the boxes
boxes = {
    0: ['crown', 'gift'],
    1: ['bag', 'map', 'plane'],
    2: ['ball', 'coffee', 'painting'],
    3: ['camera', 'tissue'],
    4: [],
    5: ['drug', 'medicine', 'picture'],
    6: ['bowl', 'bread', 'train'],
}

# Define the moves
moves = [
    (None, 0, 'shell'),        # Put the shell into Box 0
    (0, None, 'gift'),         # Remove the gift from Box 0
    (0, None, 'shell'),        # Remove the shell from Box 0
    (1, 0, 'map'),             # Move the map from Box 1 to Box 0
    (1, 0, 'plane'),           # Move the plane from Box 1 to Box 0
    (None, 3, 'mirror'),       # Put the mirror into Box 3
    (6, None, 'bowl'),         # Remove the bowl from Box 6
    (6, None, 'bread'),        # Remove the bread from Box 6
    (6, None, 'train'),        # Remove the train from Box 6
    (1, None, 'bag'),          # Remove the bag from Box 1
    (2, None, 'ball'),         # Remove the ball from Box 2
    (2, None, 'painting'),     # Remove the painting from Box 2
    (None, 6, 'beer'),         # Put the beer into Box 6
    (None, 6, 'letter'),       # Put the letter into Box 6
    (None, 1, 'ball'),         # Put the ball into Box 1
    (None, 1, 'shoe'),         # Put the shoe into Box 1
    (0, None, 'crown'),        # Remove the crown from Box 0
    (0, None, 'plane'),        # Remove the plane from Box 0
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