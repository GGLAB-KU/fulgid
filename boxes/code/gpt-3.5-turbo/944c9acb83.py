# Initialize the boxes
boxes = {
    0: ['cash', 'crown', 'cup'],
    1: ['brain', 'chemical', 'glass'],
    2: ['drink'],
    3: [],
    4: [],
    5: ['wire'],
    6: ['ticket'],
}

# Define the moves
moves = [
    (0, 2, 'cash'),         # Move the cash from Box 0 to Box 2
    (2, 4, 'cash'),         # Move the cash from Box 2 to Box 4
    (1, None, 'glass'),     # Remove the glass from Box 1
    (0, 1, 'crown'),        # Move the crown from Box 0 to Box 1
    (1, None, 'crown'),     # Remove the crown from Box 1
    (0, None, 'cup'),       # Remove the cup from Box 0
    (6, None, 'ticket'),    # Remove the ticket from Box 6
    (4, 1, 'drink'),        # Move the drink from Box 4 to Box 1
    (None, 0, 'clock'),     # Put the clock into Box 0
    (4, 2, 'cash'),         # Move the cash from Box 4 to Box 2
    (0, None, 'clock'),     # Remove the clock from Box 0
    (5, None, 'wire')       # Remove the wire from Box 5
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