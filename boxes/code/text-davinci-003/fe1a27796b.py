# Initialize the boxes
boxes = {
    0: ['bottle', 'dish', 'fish'],
    1: ['ring', 'ticket'],
    2: ['bread', 'drink', 'map'],
    3: ['knife'],
    4: ['shell'],
    5: ['bag'],
    6: ['document', 'picture', 'pot'],
}

# Define the moves
moves = [
    (6, None, 'document'),   # Remove the document from Box 6
    (6, None, 'pot'),        # Remove the pot from Box 6
    (4, None, 'shell'),      # Remove the shell from Box 4
    (None, 3, 'coffee'),     # Put the coffee into Box 3
    (3, 6, 'coffee'),        # Move the coffee from Box 3 to Box 6
    (3, 6, 'knife'),         # Move the knife from Box 3 to Box 6
    (2, None, 'bread'),      # Remove the bread from Box 2
    (2, None, 'drink'),      # Remove the drink from Box 2
    (2, None, 'map'),        # Remove the map from Box 2
    (0, None, 'bottle'),     # Remove the bottle from Box 0
    (None, 3, 'radio'),      # Put the radio into Box 3
    (6, None, 'picture'),    # Remove the picture from Box 6
    (5, 2, 'bag'),           # Move the bag from Box 5 to Box 2
    (None, 1, 'drink')       # Put the drink into Box 1
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