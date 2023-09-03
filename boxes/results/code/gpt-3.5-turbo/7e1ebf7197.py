# Initialize the boxes
boxes = {
    0: ['branch', 'fig'],
    1: ['cake', 'cash', 'ice'],
    2: ['clock'],
    3: [],
    4: ['fish', 'string'],
    5: ['bus'],
    6: ['note'],
}

# Define the moves
moves = [
    (6, 4, 'note'),         # Move the note from Box 6 to Box 4
    (2, 5, 'clock'),        # Move the clock from Box 2 to Box 5
    (1, 5, 'ice'),          # Move the ice from Box 1 to Box 5
    (None, 6, 'wheel'),     # Put the wheel into Box 6
    (1, None, 'cake'),      # Remove the cake from Box 1
    (1, None, 'cash'),      # Remove the cash from Box 1
    (5, 2, 'clock'),        # Move the clock from Box 5 to Box 2
    (5, 2, 'ice'),          # Move the ice from Box 5 to Box 2
    (4, 5, 'note'),         # Move the note from Box 4 to Box 5
    (4, 5, 'string'),       # Move the string from Box 4 to Box 5
    (None, 3, 'sheet'),     # Put the sheet into Box 3
    (4, None, 'fish'),      # Remove the fish from Box 4
    (5, 0, 'note'),         # Move the note from Box 5 to Box 0
    (0, None, 'branch'),    # Remove the branch from Box 0
    (0, None, 'fig')        # Remove the fig from Box 0
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