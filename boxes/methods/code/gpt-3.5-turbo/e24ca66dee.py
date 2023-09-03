# Initialize the boxes
boxes = {
    0: ['magazine'],
    1: ['boat'],
    2: ['cash', 'shirt'],
    3: ['bottle', 'egg'],
    4: ['bone'],
    5: ['cup', 'phone', 'plant'],
    6: [],
}

# Define the moves
moves = [
    (0, 1, 'magazine'),     # Move the magazine from Box 0 to Box 1
    (1, None, 'boat'),      # Remove the boat from Box 1
    (1, None, 'magazine'),  # Remove the magazine from Box 1
    (2, None, 'cash'),      # Remove the cash from Box 2
    (2, None, 'shirt'),     # Remove the shirt from Box 2
    (5, 2, 'phone'),        # Move the phone from Box 5 to Box 2
    (5, 2, 'plant'),        # Move the plant from Box 5 to Box 2
    (None, 0, 'machine'),   # Put the machine into Box 0
    (None, 0, 'ticket'),    # Put the ticket into Box 0
    (0, 6, 'ticket'),       # Move the ticket from Box 0 to Box 6
    (4, None, 'crown'),     # Put the crown into Box 4
    (3, None, 'bottle'),    # Remove the bottle from Box 3
    (3, None, 'egg'),       # Remove the egg from Box 3
    (5, None, 'cup'),       # Remove the cup from Box 5
    (2, 1, 'plant'),        # Move the plant from Box 2 to Box 1
    (1, 2, 'plant'),        # Move the plant from Box 1 to Box 2
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