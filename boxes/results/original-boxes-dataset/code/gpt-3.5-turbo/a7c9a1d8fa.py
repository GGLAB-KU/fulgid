# Initialize the boxes
boxes = {
    0: ['bus', 'watch'],
    1: [],
    2: ['dress', 'note', 'sheet'],
    3: ['bowl', 'computer', 'paper'],
    4: ['boat', 'dish', 'television'],
    5: ['boot', 'rose'],
    6: [],
}

# Define the moves
moves = [
    (0, None, 'bus'),        # Remove the bus from Box 0
    (5, 0, 'boot'),          # Move the boot from Box 5 to Box 0
    (5, 0, 'rose'),          # Move the rose from Box 5 to Box 0
    (0, None, 'boot'),       # Remove the boot from Box 0
    (0, None, 'rose'),       # Remove the rose from Box 0
    (0, None, 'watch'),      # Remove the watch from Box 0
    (None, 0, 'bag'),        # Put the bag into Box 0
    (4, None, 'boat'),       # Remove the boat from Box 4
    (4, None, 'television'), # Remove the television from Box 4
    (4, 1, 'dish'),          # Move the dish from Box 4 to Box 1
    (2, None, 'dress'),      # Remove the dress from Box 2
    (2, None, 'note'),       # Remove the note from Box 2
    (0, None, 'bag'),        # Remove the bag from Box 0
    (3, 0, 'paper'),         # Move the paper from Box 3 to Box 0
    (0, None, 'paper'),      # Remove the paper from Box 0
    (None, 2, 'boot'),       # Put the boot into Box 2
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