# Initialize the boxes
boxes = {
    0: ['tie'],
    1: ['bus', 'cream'],
    2: ['ball', 'bill'],
    3: ['bomb', 'car'],
    4: ['brick', 'sheet', 'wire'],
    5: ['knife', 'phone', 'train'],
    6: [],
}

# Define the moves
moves = [
    (4, None, 'sheet'),     # Remove the sheet from Box 4
    (4, None, 'wire'),      # Remove the wire from Box 4
    (1, 0, 'bus'),          # Move the bus from Box 1 to Box 0
    (1, 0, 'cream'),        # Move the cream from Box 1 to Box 0
    (0, None, 'bus'),       # Remove the bus from Box 0
    (0, None, 'cream'),     # Remove the cream from Box 0
    (5, None, 'phone'),     # Remove the phone from Box 5
    (5, None, 'train'),     # Remove the train from Box 5
    (4, None, 'brick'),     # Remove the brick from Box 4
    (0, None, 'tie'),       # Remove the tie from Box 0
    (None, 0, 'milk'),      # Put the milk into Box 0
    (3, 5, 'bomb'),         # Move the bomb from Box 3 to Box 5
    (3, 0, 'car'),          # Move the car from Box 3 to Box 0
    (5, None, 'bomb'),      # Remove the bomb from Box 5
    (5, None, 'knife'),     # Remove the knife from Box 5
    (0, None, 'milk'),      # Remove the milk from Box 0
    (None, 1, 'boat'),      # Put the boat into Box 1
    (None, 1, 'magazine')   # Put the magazine into Box 1
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