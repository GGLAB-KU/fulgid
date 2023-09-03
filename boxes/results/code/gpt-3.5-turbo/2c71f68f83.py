# Initialize the boxes
boxes = {
    0: ['cheese', 'dish', 'picture'],
    1: ['cigarette'],
    2: [],
    3: ['disk', 'map', 'meat'],
    4: ['boot', 'flower'],
    5: ['bag', 'cross', 'machine'],
    6: ['ticket'],
}

# Define the moves
moves = [
    (5, None, 'bag'),       # Remove the bag from Box 5
    (5, None, 'cross'),     # Remove the cross from Box 5
    (5, None, 'machine'),   # Remove the machine from Box 5
    (None, 5, 'apple'),     # Put the apple into Box 5
    (6, None, 'ticket'),    # Remove the ticket from Box 6
    (5, 4, 'apple'),        # Move the apple from Box 5 to Box 4
    (4, None, 'apple'),     # Remove the apple from Box 4
    (None, 2, 'clock'),     # Put the clock into Box 2
    (None, 5, 'stone'),     # Put the stone into Box 5
    (2, None, 'clock'),     # Remove the clock from Box 2
    (5, None, 'stone'),     # Remove the stone from Box 5
    (4, 5, 'flower'),       # Move the flower from Box 4 to Box 5
    (4, 5, 'boot'),         # Move the boot from Box 4 to Box 5
    (0, 4, 'cheese'),       # Move the cheese from Box 0 to Box 4
    (0, 4, 'dish')          # Move the dish from Box 0 to Box 4
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