# Initialize the boxes
boxes = {
    0: ['bus', 'car', 'fan'],
    1: ['boot', 'camera', 'tissue'],
    2: [],
    3: ['phone', 'wheel'],
    4: ['note'],
    5: ['map'],
    6: ['ball', 'beer'],
}

# Define the moves
moves = [
    (5, None, 'map'),       # Remove the map from Box 5
    (0, 4, 'bus'),          # Move the bus from Box 0 to Box 4
    (4, None, 'bus'),       # Remove the bus from Box 4
    (4, None, 'note'),      # Remove the note from Box 4
    (3, None, 'phone'),     # Remove the phone from Box 3
    (3, None, 'wheel'),     # Remove the wheel from Box 3
    (0, 4, 'car'),          # Move the car from Box 0 to Box 4
    (0, 4, 'fan'),          # Move the fan from Box 0 to Box 4
    (6, 0, 'beer'),         # Move the beer from Box 6 to Box 0
    (1, None, 'boot'),      # Remove the boot from Box 1
    (1, None, 'tissue')     # Remove the tissue from Box 1
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