# Initialize the boxes
boxes = {
    0: ['rose', 'suit'],
    1: ['key', 'paper', 'shoe'],
    2: ['magazine'],
    3: ['bag', 'cheese', 'stone'],
    4: ['fish', 'map', 'rock'],
    5: ['note'],
    6: ['crown'],
}

# Define the moves
moves = [
    (1, 5, 'paper'),    # Move the paper from Box 1 to Box 5
    (1, 5, 'shoe'),     # Move the shoe from Box 1 to Box 5
    (None, 6, 'fan'),   # Put the fan into Box 6
    (None, 6, 'shell'), # Put the shell into Box 6
    (6, 2, 'crown'),    # Move the crown from Box 6 to Box 2
    (6, 2, 'shell'),    # Move the shell from Box 6 to Box 2
    (4, 6, 'map'),      # Move the map from Box 4 to Box 6
    (4, 6, 'rock'),     # Move the rock from Box 4 to Box 6
    (None, 4, 'book'),  # Put the book into Box 4
    (6, None, 'map'),   # Remove the map from Box 6
    (3, None, 'stone'), # Remove the stone from Box 3
    (2, 1, 'magazine'), # Move the magazine from Box 2 to Box 1
    (2, 1, 'shell'),    # Move the shell from Box 2 to Box 1
    (None, 0, 'tie'),   # Put the tie into Box 0
    (2, 6, 'crown'),    # Move the crown from Box 2 to Box 6
    (None, 3, 'ticket') # Put the ticket into Box 3
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