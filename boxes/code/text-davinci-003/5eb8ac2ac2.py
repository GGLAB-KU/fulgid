# Initialize the boxes
boxes = {
    0: ['bill', 'fig', 'pipe'],
    1: ['train'],
    2: ['machine', 'phone'],
    3: ['meat', 'plant'],
    4: ['boat', 'leaf'],
    5: [],
    6: ['drug', 'paper'],
}

# Define the moves
moves = [
    (2, None, 'phone'),       # Remove the phone from Box 2
    (6, 1, 'drug'),           # Move the drug from Box 6 to Box 1
    (6, 1, 'paper'),          # Move the paper from Box 6 to Box 1
    (None, 3, 'television'),   # Put the television into Box 3
    (0, 2, 'bill'),           # Move the bill from Box 0 to Box 2
    (0, 2, 'fig'),            # Move the fig from Box 0 to Box 2
    (1, None, 'drug'),        # Remove the drug from Box 1
    (1, None, 'paper'),       # Remove the paper from Box 1
    (1, None, 'train'),       # Remove the train from Box 1
    (None, 4, 'jacket'),      # Put the jacket into Box 4
    (2, None, 'bill'),        # Remove the bill from Box 2
    (2, None, 'fig'),         # Remove the fig from Box 2
    (2, None, 'machine'),     # Remove the machine from Box 2
    (None, 2, 'fish'),        # Put the fish into Box 2
    (3, 1, 'meat'),           # Move the meat from Box 3 to Box 1
    (3, 1, 'television'),     # Move the television from Box 3 to Box 1
    (0, None, 'pipe'),        # Remove the pipe from Box 0
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