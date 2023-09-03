# Initialize the boxes
boxes = {
    0: ['bell', 'tape'],
    1: ['picture', 'television'],
    2: ['ball', 'boot', 'fish'],
    3: ['branch', 'guitar', 'leaf'],
    4: ['creature', 'map', 'sheet'],
    5: ['cream', 'ice', 'plant'],
    6: ['string'],
}

# Define the moves
moves = [
    (4, 0, 'sheet'),        # Move the sheet from Box 4 to Box 0
    (1, None, 'picture'),   # Remove the picture from Box 1
    (0, None, 'tape'),      # Remove the tape from Box 0
    (6, None, 'string'),    # Remove the string from Box 6
    (5, 1, 'ice'),          # Move the ice from Box 5 to Box 1
    (None, 1, 'shell'),     # Put the shell into Box 1
    (5, None, 'cream'),     # Remove the cream from Box 5
    (5, None, 'plant'),     # Remove the plant from Box 5
    (4, None, 'creature'),  # Remove the creature from Box 4
    (1, 5, 'ice'),          # Move the ice from Box 1 to Box 5
    (1, 5, 'shell'),        # Move the shell from Box 1 to Box 5
    (1, 5, 'television'),   # Move the television from Box 1 to Box 5
    (None, 1, 'apple'),     # Put the apple into Box 1
    (None, 1, 'coat'),      # Put the coat into Box 1
    (None, 6, 'plane'),     # Put the plane into Box 6
    (2, 1, 'fish'),         # Move the fish from Box 2 to Box 1
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