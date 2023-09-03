# Initialize the boxes
boxes = {
    0: [],
    1: ['book', 'clock', 'rose'],
    2: ['tie'],
    3: ['fig', 'painting'],
    4: ['ball', 'glass', 'stone'],
    5: ['radio', 'train'],
    6: ['coffee'],
}

# Define the moves
moves = [
    (5, 2, 'radio'),    # Move the radio from Box 5 to Box 2
    (1, None, 'book'),  # Remove the book from Box 1
    (5, None, 'train'), # Remove the train from Box 5
    (4, None, 'glass'), # Remove the glass from Box 4
    (2, None, 'radio'), # Remove the radio from Box 2
    (1, None, 'rose'),  # Remove the rose from Box 1
    (1, None, 'clock'), # Remove the clock from Box 1
    (4, None, 'ball'),  # Remove the ball from Box 4
    (4, None, 'stone'), # Remove the stone from Box 4
    (None, 6, 'disk'),  # Put the disk into Box 6
    (2, None, 'tie')    # Remove the tie from Box 2
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