# Initialize the boxes
boxes = {
    0: ['phone', 'seed', 'tissue'],
    1: ['mirror', 'suit'],
    2: ['brick', 'television'],
    3: ['cream', 'dish', 'hat'],
    4: [],
    5: ['cheese', 'game', 'glass'],
    6: ['card', 'wheel'],
}

# Define the moves
moves = [
    (5, None, 'game'),       # Remove the game from Box 5
    (5, None, 'glass'),      # Remove the glass from Box 5
    (6, None, 'wheel'),      # Remove the wheel from Box 6
    (None, 1, 'tape'),       # Put the tape into Box 1
    (None, 6, 'meat'),       # Put the meat into Box 6
    (3, None, 'cream'),      # Remove the cream from Box 3
    (3, None, 'hat'),        # Remove the hat from Box 3
    (2, None, 'brick'),      # Remove the brick from Box 2
    (2, None, 'television'), # Remove the television from Box 2
    (None, 2, 'bomb'),       # Put the bomb into Box 2
    (None, 2, 'crown'),      # Put the crown into Box 2
    (5, 6, 'cheese'),        # Move the cheese from Box 5 to Box 6
    (0, None, 'phone'),      # Remove the phone from Box 0
    (0, None, 'tissue'),     # Remove the tissue from Box 0
    (2, 3, 'crown'),         # Move the crown from Box 2 to Box 3
    (2, 3, 'bomb'),          # Move the bomb from Box 2 to Box 3
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