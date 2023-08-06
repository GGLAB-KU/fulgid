# Initialize the boxes
boxes = {
    0: ['cigarette'],
    1: ['drug', 'fig'],
    2: ['brain', 'pot'],
    3: ['coffee'],
    4: ['egg', 'string', 'tissue'],
    5: ['map'],
    6: ['boat', 'plane'],
}

# Define the moves
moves = [
    (None, 2, 'card'),       # Put the card into Box 2
    (1, None, 'fig'),        # Remove the fig from Box 1
    (2, None, 'brain'),      # Remove the brain from Box 2
    (2, None, 'card'),       # Remove the card from Box 2
    (2, None, 'pot'),        # Remove the pot from Box 2
    (5, 0, 'map'),           # Move the map from Box 5 to Box 0
    (4, 5, 'egg'),           # Move the egg from Box 4 to Box 5
    (4, 5, 'string'),        # Move the string from Box 4 to Box 5
    (4, 5, 'tissue'),        # Move the tissue from Box 4 to Box 5
    (6, None, 'boat'),       # Remove the boat from Box 6
    (0, 1, 'map'),           # Move the map from Box 0 to Box 1
    (None, 4, 'ball'),       # Put the ball into Box 4
    (None, 4, 'sheet'),      # Put the sheet into Box 4
    (1, 2, 'drug'),          # Move the drug from Box 1 to Box 2
    (1, 2, 'map'),           # Move the map from Box 1 to Box 2
    (6, 1, 'plane'),         # Move the plane from Box 6 to Box 1
    (0, 2, 'cigarette'),     # Move the cigarette from Box 0 to Box 2
    (None, 1, 'bus'),        # Put the bus into Box 1
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