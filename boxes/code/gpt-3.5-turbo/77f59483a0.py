# Initialize the boxes
boxes = {
    0: ['drink', 'wheel'],
    1: [],
    2: ['coat'],
    3: ['tea'],
    4: ['brain', 'creature', 'pot'],
    5: ['crown', 'ticket'],
    6: ['computer', 'engine', 'suit'],
}

# Define the moves
moves = [
    (0, None, 'wheel'),       # Remove the wheel from Box 0
    (3, None, 'tea'),         # Remove the tea from Box 3
    (5, None, 'crown'),       # Remove the crown from Box 5
    (5, None, 'ticket'),      # Remove the ticket from Box 5
    (None, 0, 'bomb'),        # Put the bomb into Box 0
    (6, 3, 'suit'),           # Move the suit from Box 6 to Box 3
    (4, None, 'creature'),    # Remove the creature from Box 4
    (4, None, 'pot'),         # Remove the pot from Box 4
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