# Initialize the boxes
boxes = {
    0: ['dress', 'tape', 'tie'],
    1: ['picture'],
    2: ['document', 'drug', 'glass'],
    3: ['meat'],
    4: [],
    5: ['brain', 'pipe'],
    6: ['boat', 'boot'],
}

# Define the moves
moves = [
    (2, 4, 'drug'),         # Move the drug from Box 2 to Box 4
    (3, 2, 'meat'),         # Move the meat from Box 3 to Box 2
    (5, None, 'brain'),     # Remove the brain from Box 5
    (5, None, 'pipe'),      # Remove the pipe from Box 5
    (0, 4, 'dress'),        # Move the dress from Box 0 to Box 4
    (0, 4, 'tape'),         # Move the tape from Box 0 to Box 4
    (0, None, 'tie'),       # Remove the tie from Box 0
    (None, 5, 'brain'),     # Put the brain into Box 5
    (5, 0, 'brain'),        # Move the brain from Box 5 to Box 0
    (6, None, 'boat'),      # Remove the boat from Box 6
    (None, 0, 'bell'),      # Put the bell into Box 0
    (None, 0, 'television'), # Put the television into Box 0
    (4, 3, 'dress'),        # Move the dress from Box 4 to Box 3
    (4, 3, 'drug'),         # Move the drug from Box 4 to Box 3
    (4, 5, 'tape'),         # Move the tape from Box 4 to Box 5
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