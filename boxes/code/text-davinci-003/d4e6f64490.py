# Initialize the boxes
boxes = {
    0: ['engine'],
    1: ['bottle'],
    2: ['letter'],
    3: ['brain', 'shoe', 'ticket'],
    4: ['egg', 'map'],
    5: ['cake', 'crown', 'medicine'],
    6: ['cream', 'drug'],
}

# Define the moves
moves = [
    (None, 4, 'gift'),       # Put the gift into Box 4
    (None, 6, 'wheel'),      # Put the wheel into Box 6
    (5, 2, 'crown'),         # Move the crown from Box 5 to Box 2
    (5, 2, 'medicine'),      # Move the medicine from Box 5 to Box 2
    (None, 1, 'pipe'),       # Put the pipe into Box 1
    (1, None, 'bottle'),     # Remove the bottle from Box 1
    (1, None, 'pipe'),       # Remove the pipe from Box 1
    (6, 1, 'wheel'),         # Move the wheel from Box 6 to Box 1
    (3, None, 'ticket'),     # Remove the ticket from Box 3
    (3, None, 'shoe'),       # Remove the shoe from Box 3
    (None, 0, 'boat'),       # Put the boat into Box 0
    (3, 1, 'brain'),         # Move the brain from Box 3 to Box 1
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