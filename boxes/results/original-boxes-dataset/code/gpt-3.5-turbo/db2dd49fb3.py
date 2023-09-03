# Initialize the boxes
boxes = {
    0: ['plant'],
    1: ['bill', 'cigarette', 'creature'],
    2: ['beer', 'cash', 'cup'],
    3: ['jacket', 'key', 'shoe'],
    4: ['television'],
    5: ['computer', 'ticket'],
    6: ['car'],
}

# Define the moves
moves = [
    (1, 5, 'creature'),     # Move the creature from Box 1 to Box 5
    (5, None, 'computer'),  # Remove the computer from Box 5
    (5, None, 'creature'),  # Remove the creature from Box 5
    (4, None, 'television'), # Remove the television from Box 4
    (None, 1, 'suit'),      # Put the suit into Box 1
    (2, None, 'beer'),      # Remove the beer from Box 2
    (2, None, 'cash'),      # Remove the cash from Box 2
    (2, None, 'cup'),       # Remove the cup from Box 2
    (3, None, 'key'),       # Remove the key from Box 3
    (3, None, 'shoe'),      # Remove the shoe from Box 3
    (6, 3, 'car'),          # Move the car from Box 6 to Box 3
    (3, None, 'car'),       # Remove the car from Box 3
    (0, 5, 'plant'),        # Move the plant from Box 0 to Box 5
    (5, None, 'plant'),     # Remove the plant from Box 5
    (5, None, 'ticket'),    # Remove the ticket from Box 5
    (None, 5, 'leaf')       # Put the leaf into Box 5
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