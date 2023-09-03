# Initialize the boxes
boxes = {
    0: ['bell', 'jacket'],
    1: ['newspaper', 'sheet'],
    2: ['flower', 'milk'],
    3: ['bread', 'machine'],
    4: ['drug', 'tape'],
    5: ['apple', 'meat'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'bread'),       # Remove the bread from Box 3
    (2, None, 'flower'),      # Remove the flower from Box 2
    (2, None, 'milk'),        # Remove the milk from Box 2
    (4, 3, 'drug'),           # Move the drug from Box 4 to Box 3
    (4, 3, 'tape'),           # Move the tape from Box 4 to Box 3
    (1, None, 'sheet'),       # Remove the sheet from Box 1
    (1, 0, 'newspaper'),      # Move the newspaper from Box 1 to Box 0
    (5, None, 'meat'),        # Remove the meat from Box 5
    (None, 5, 'ice'),         # Put the ice into Box 5
    (None, 2, 'chemical'),    # Put the chemical into Box 2
    (None, 2, 'disk'),        # Put the disk into Box 2
    (None, 2, 'picture'),     # Put the picture into Box 2
    (None, 5, 'letter'),      # Put the letter into Box 5
    (None, 1, 'tea'),         # Put the tea into Box 1
    (None, 1, 'cream'),       # Put the cream into Box 1
    (None, 1, 'pipe'),        # Put the pipe into Box 1
    (1, None, 'cream')        # Remove the cream from Box 1
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