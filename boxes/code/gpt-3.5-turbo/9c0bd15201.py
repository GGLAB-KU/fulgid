# Initialize the boxes
boxes = {
    0: ['note', 'suit'],
    1: [],
    2: [],
    3: ['glass'],
    4: ['document', 'newspaper', 'tape'],
    5: ['clock', 'wheel'],
    6: ['stone'],
}

# Define the moves
moves = [
    (3, 2, 'glass'),        # Move the glass from Box 3 to Box 2
    (5, None, 'clock'),     # Remove the clock from Box 5
    (5, None, 'wheel'),     # Remove the wheel from Box 5
    (4, 1, 'newspaper'),    # Move the newspaper from Box 4 to Box 1
    (1, 2, 'newspaper'),    # Move the newspaper from Box 1 to Box 2
    (6, 3, 'stone'),        # Move the stone from Box 6 to Box 3
    (None, 1, 'drug'),      # Put the drug into Box 1
    (None, 1, 'phone'),     # Put the phone into Box 1
    (4, 0, 'document'),     # Move the document from Box 4 to Box 0
    (0, 6, 'document'),     # Move the document from Box 0 to Box 6
    (0, 6, 'note'),         # Move the note from Box 0 to Box 6
    (2, None, 'newspaper'), # Remove the newspaper from Box 2
    (4, 3, 'tape'),         # Move the tape from Box 4 to Box 3
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