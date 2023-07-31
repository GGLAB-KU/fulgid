# Initialize the boxes
boxes = {
    0: ['shell', 'stone'],
    1: ['cigarette', 'disk', 'shirt'],
    2: ['bill', 'wire'],
    3: ['key'],
    4: ['computer'],
    5: ['ice', 'paper'],
    6: ['brick', 'fan', 'map'],
}

# Define the moves
moves = [
    (5, None, 'ice'),       # Remove the ice from Box 5
    (2, 4, 'bill'),         # Move the bill from Box 2 to Box 4
    (1, None, 'cigarette'), # Remove the cigarette from Box 1
    (1, None, 'disk'),      # Remove the disk from Box 1
    (2, None, 'wire'),      # Remove the wire from Box 2
    (6, 5, 'fan'),          # Move the fan from Box 6 to Box 5
    (3, 5, 'key'),          # Move the key from Box 3 to Box 5
    (None, 1, 'branch'),    # Put the branch into Box 1
    (None, 6, 'wheel'),     # Put the wheel into Box 6
    (1, 0, 'branch'),       # Move the branch from Box 1 to Box 0
    (5, None, 'fan'),       # Remove the fan from Box 5
    (5, None, 'paper'),     # Remove the paper from Box 5
    (None, 3, 'beer'),      # Put the beer into Box 3
    (None, 3, 'brain'),     # Put the brain into Box 3
    (None, 3, 'mirror')     # Put the mirror into Box 3
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