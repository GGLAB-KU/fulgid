# Initialize the boxes
boxes = {
    0: [],
    1: ['jacket', 'note', 'ticket'],
    2: ['branch', 'cream'],
    3: ['letter'],
    4: ['apple', 'medicine', 'watch'],
    5: ['brick'],
    6: ['fish', 'rose'],
}

# Define the moves
moves = [
    (6, None, 'fish'),       # Remove the fish from Box 6
    (6, None, 'rose'),       # Remove the rose from Box 6
    (5, None, 'brick'),      # Remove the brick from Box 5
    (4, 6, 'apple'),         # Move the apple from Box 4 to Box 6
    (4, 6, 'medicine'),      # Move the medicine from Box 4 to Box 6
    (2, 5, 'branch'),        # Move the branch from Box 2 to Box 5
    (2, 5, 'cream'),         # Move the cream from Box 2 to Box 5
    (None, 0, 'paper'),      # Put the paper into Box 0
    (4, 2, 'watch'),         # Move the watch from Box 4 to Box 2
    (1, 4, 'ticket'),        # Move the ticket from Box 1 to Box 4
    (4, None, 'ticket')      # Remove the ticket from Box 4
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