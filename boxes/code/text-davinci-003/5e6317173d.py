# Initialize the boxes
boxes = {
    0: ['creature'],
    1: ['cash', 'drug'],
    2: ['letter', 'magazine', 'ring'],
    3: [],
    4: [],
    5: ['coffee', 'rock', 'ticket'],
    6: [],
}

# Define the moves
moves = [
    (2, 6, 'letter'),       # Move the letter from Box 2 to Box 6
    (None, 6, 'crown'),     # Put the crown into Box 6
    (0, 4, 'creature'),     # Move the creature from Box 0 to Box 4
    (None, 4, 'milk'),      # Put the milk into Box 4
    (None, 4, 'sheet'),     # Put the sheet into Box 4
    (1, None, 'cash'),      # Remove the cash from Box 1
    (6, None, 'crown'),     # Remove the crown from Box 6
    (5, None, 'coffee'),    # Remove the coffee from Box 5
    (5, None, 'ticket'),    # Remove the ticket from Box 5
    (4, 6, 'sheet'),        # Move the sheet from Box 4 to Box 6
    (None, 4, 'train'),     # Put the train into Box 4
    (6, None, 'sheet')      # Remove the sheet from Box 6
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