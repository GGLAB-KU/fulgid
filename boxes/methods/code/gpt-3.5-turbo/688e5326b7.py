# Initialize the boxes
boxes = {
    0: ['picture', 'shoe'],
    1: ['bell', 'coffee', 'sheet'],
    2: ['glass'],
    3: ['chemical', 'pot'],
    4: ['boot'],
    5: [],
    6: ['document', 'file', 'gift'],
}

# Define the moves
moves = [
    (1, 4, 'bell'),         # Move the bell from Box 1 to Box 4
    (1, 4, 'sheet'),        # Move the sheet from Box 1 to Box 4
    (None, 0, 'drink'),     # Put the drink into Box 0
    (None, 2, 'cigarette'), # Put the cigarette into Box 2
    (None, 2, 'newspaper'), # Put the newspaper into Box 2
    (0, None, 'shoe'),      # Remove the shoe from Box 0
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