# Initialize the boxes
boxes = {
    0: ['block', 'computer', 'cream'],
    1: [],
    2: ['radio'],
    3: ['apple', 'fan'],
    4: ['tea'],
    5: ['boot', 'branch', 'watch'],
    6: ['clock'],
}

# Define the moves
moves = [
    (3, 1, 'fan'),          # Move the fan from Box 3 to Box 1
    (None, 2, 'stone'),     # Put the stone into Box 2
    (6, 2, 'clock'),        # Move the clock from Box 6 to Box 2
    (None, 4, 'bill'),      # Put the bill into Box 4
    (None, 4, 'map'),       # Put the map into Box 4
    (4, 6, 'bill'),         # Move the bill from Box 4 to Box 6
    (4, 6, 'map'),          # Move the map from Box 4 to Box 6
    (4, 6, 'tea'),          # Move the tea from Box 4 to Box 6
    (5, 3, 'boot'),         # Move the boot from Box 5 to Box 3
    (5, 3, 'watch'),        # Move the watch from Box 5 to Box 3
    (2, 1, 'radio'),        # Move the radio from Box 2 to Box 1
    (2, 1, 'stone'),        # Move the stone from Box 2 to Box 1
    (5, None, 'branch'),    # Remove the branch from Box 5
    (6, None, 'tea'),       # Remove the tea from Box 6
    (None, 6, 'cigarette'), # Put the cigarette into Box 6
    (6, 4, 'bill'),         # Move the bill from Box 6 to Box 4
    (6, 4, 'cigarette')     # Move the cigarette from Box 6 to Box 4
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