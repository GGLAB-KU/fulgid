# Initialize the boxes
boxes = {
    0: ['car', 'crown', 'shoe'],
    1: ['camera', 'drink', 'engine'],
    2: ['plate'],
    3: ['creature'],
    4: ['coffee', 'ice', 'meat'],
    5: ['bill', 'chemical', 'letter'],
    6: ['phone'],
}

# Define the moves
moves = [
    (6, None, 'phone'),       # Remove the phone from Box 6
    (0, None, 'car'),         # Remove the car from Box 0
    (0, None, 'crown'),       # Remove the crown from Box 0
    (0, None, 'shoe'),        # Remove the shoe from Box 0
    (3, None, 'creature'),    # Remove the creature from Box 3
    (4, None, 'ice'),         # Remove the ice from Box 4
    (2, None, 'plate'),       # Remove the plate from Box 2
    (4, 3, 'coffee'),         # Move the coffee from Box 4 to Box 3
    (1, None, 'camera'),      # Remove the camera from Box 1
    (1, None, 'drink'),       # Remove the drink from Box 1
    (1, None, 'engine'),      # Remove the engine from Box 1
    (4, None, 'meat'),        # Remove the meat from Box 4
    (None, 2, 'bus'),         # Put the bus into Box 2
    (None, 1, 'boat')         # Put the boat into Box 1
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