# Initialize the boxes
boxes = {
    0: ['jacket', 'key', 'stone'],
    1: ['fig', 'file', 'glass'],
    2: ['disk', 'shirt'],
    3: ['cigarette', 'tape', 'tie'],
    4: ['document', 'guitar'],
    5: ['train'],
    6: ['hat', 'newspaper', 'pot'],
}

# Define the moves
moves = [
    (0, None, 'jacket'),    # Remove the jacket from Box 0
    (0, None, 'key'),       # Remove the key from Box 0
    (0, None, 'stone'),     # Remove the stone from Box 0
    (5, 0, 'train'),        # Move the train from Box 5 to Box 0
    (1, None, 'fig'),       # Remove the fig from Box 1
    (1, None, 'glass'),     # Remove the glass from Box 1
    (1, 2, 'file'),         # Move the file from Box 1 to Box 2
    (3, 0, 'tape'),         # Move the tape from Box 3 to Box 0
    (3, 0, 'tie'),          # Move the tie from Box 3 to Box 0
    (0, 5, 'tape'),         # Move the tape from Box 0 to Box 5
    (0, 5, 'tie'),          # Move the tie from Box 0 to Box 5
    (6, 4, 'pot'),          # Move the pot from Box 6 to Box 4
    (0, None, 'train'),     # Remove the train from Box 0
    (None, 0, 'note'),      # Put the note into Box 0
    (None, 0, 'stone'),     # Put the stone into Box 0
    (None, 3, 'apple'),     # Put the apple into Box 3
    (None, 3, 'key'),       # Put the key into Box 3
    (None, 5, 'cream')      # Put the cream into Box 5
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