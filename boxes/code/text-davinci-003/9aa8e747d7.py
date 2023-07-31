# Initialize the boxes
boxes = {
    0: [],
    1: ['cigarette', 'hat'],
    2: ['bowl', 'stone'],
    3: ['ice', 'medicine'],
    4: ['bag'],
    5: ['file', 'seed', 'television'],
    6: ['map'],
}

# Define the moves
moves = [
    (6, None, 'map'),       # Remove the map from Box 6
    (None, 1, 'train'),     # Put the train into Box 1
    (5, None, 'seed'),      # Remove the seed from Box 5
    (5, None, 'television'),# Remove the television from Box 5
    (1, 0, 'cigarette'),    # Move the cigarette from Box 1 to Box 0
    (5, None, 'file'),      # Remove the file from Box 5
    (1, None, 'hat'),       # Remove the hat from Box 1
    (1, None, 'train'),     # Remove the train from Box 1
    (0, None, 'cigarette'), # Remove the cigarette from Box 0
    (4, 6, 'bag'),          # Move the bag from Box 4 to Box 6
    (6, 5, 'bag'),          # Move the bag from Box 6 to Box 5
    (None, 5, 'leaf'),      # Put the leaf into Box 5
    (5, None, 'bag'),       # Remove the bag from Box 5
    (2, 4, 'bowl'),         # Move the bowl from Box 2 to Box 4
    (2, 4, 'stone')         # Move the stone from Box 2 to Box 4
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