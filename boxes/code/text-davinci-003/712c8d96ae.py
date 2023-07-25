# Initialize the boxes
boxes = {
    0: ['magazine'],
    1: ['document', 'train'],
    2: ['crown'],
    3: ['letter', 'map'],
    4: ['bell', 'bus', 'cream'],
    5: ['bowl', 'fig'],
    6: ['branch', 'painting', 'sheet'],
}

# Define the moves
moves = [
    (3, None, 'letter'),    # Remove the letter from Box 3
    (3, None, 'map'),       # Remove the map from Box 3
    (4, None, 'bell'),      # Remove the bell from Box 4
    (4, None, 'bus'),       # Remove the bus from Box 4
    (5, None, 'fig'),       # Remove the fig from Box 5
    (6, None, 'painting'),  # Remove the painting from Box 6
    (6, None, 'sheet'),     # Remove the sheet from Box 6
    (2, 0, 'crown'),        # Move the crown from Box 2 to Box 0
    (4, None, 'cream'),     # Remove the cream from Box 4
    (5, None, 'bowl'),      # Remove the bowl from Box 5
    (6, 5, 'branch'),       # Move the branch from Box 6 to Box 5
    (None, 0, 'cigarette'), # Put the cigarette into Box 0
    (1, 5, 'train'),        # Move the train from Box 1 to Box 5
    (5, 1, 'branch'),       # Move the branch from Box 5 to Box 1
    (5, 1, 'train')         # Move the train from Box 5 to Box 1
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