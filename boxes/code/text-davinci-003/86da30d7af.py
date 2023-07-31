# Initialize the boxes
boxes = {
    0: ['machine'],
    1: ['pipe'],
    2: ['brain', 'tie'],
    3: ['dish', 'plate'],
    4: ['car'],
    5: ['chemical', 'rock'],
    6: ['bag', 'egg', 'newspaper'],
}

# Define the moves
moves = [
    (0, None, 'machine'),   # Remove the machine from Box 0
    (4, 2, 'car'),          # Move the car from Box 4 to Box 2
    (1, 3, 'pipe'),         # Move the pipe from Box 1 to Box 3
    (6, None, 'bag'),       # Remove the bag from Box 6
    (None, 1, 'boat'),      # Put the boat into Box 1
    (5, 0, 'chemical'),     # Move the chemical from Box 5 to Box 0
    (None, 5, 'bill')       # Put the bill into Box 5
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