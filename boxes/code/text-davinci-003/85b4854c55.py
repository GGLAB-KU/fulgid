# Initialize the boxes
boxes = {
    0: ['paper'],
    1: ['bus', 'card', 'tissue'],
    2: ['creature', 'phone'],
    3: ['camera', 'jacket', 'shirt'],
    4: ['bill', 'map'],
    5: ['bag', 'tape'],
    6: [],
}

# Define the moves
moves = [
    (4, None, 'bill'),       # Remove the bill from Box 4
    (2, 0, 'phone'),         # Move the phone from Box 2 to Box 0
    (None, 2, 'glass'),      # Put the glass into Box 2
    (None, 4, 'bread'),      # Put the bread into Box 4
    (None, 4, 'rock'),       # Put the rock into Box 4
    (4, None, 'bill'),       # Put the bill into Box 2
    (2, None, 'creature'),   # Remove the creature from Box 2
    (2, None, 'glass'),      # Remove the glass from Box 2
    (None, 0, 'painting'),   # Put the painting into Box 0
    (3, None, 'camera'),     # Remove the camera from Box 3
    (4, None, 'map'),        # Remove the map from Box 4
    (4, None, 'rock'),       # Remove the rock from Box 4
    (1, None, 'card'),       # Remove the card from Box 1
    (2, 4, 'bill'),          # Move the bill from Box 2 to Box 4
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