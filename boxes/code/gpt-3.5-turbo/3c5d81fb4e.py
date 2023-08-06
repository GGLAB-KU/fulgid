# Initialize the boxes
boxes = {
    0: [],
    1: ['coat', 'shell', 'television'],
    2: ['boat', 'crown', 'key'],
    3: ['cross', 'dish'],
    4: ['fish', 'train', 'wheel'],
    5: ['painting', 'plant', 'ring'],
    6: ['magazine'],
}

# Define the moves
moves = [
    (None, 3, 'leaf'),       # Put the leaf into Box 3
    (2, None, 'boat'),       # Remove the boat from Box 2
    (2, None, 'crown'),      # Remove the crown from Box 2
    (6, 2, 'magazine'),      # Move the magazine from Box 6 to Box 2
    (3, None, 'dish'),       # Remove the dish from Box 3
    (None, 3, 'drink'),      # Put the drink into Box 3
    (4, None, 'train'),      # Remove the train from Box 4
    (2, 6, 'key'),           # Move the key from Box 2 to Box 6
    (2, None, 'magazine'),   # Remove the magazine from Box 2
    (4, 2, 'fish'),          # Move the fish from Box 4 to Box 2
    (4, 2, 'wheel'),         # Move the wheel from Box 4 to Box 2
    (6, None, 'key')         # Remove the key from Box 6
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