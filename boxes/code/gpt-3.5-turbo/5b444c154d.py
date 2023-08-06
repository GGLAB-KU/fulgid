# Initialize the boxes
boxes = {
    0: ['shoe'],
    1: [],
    2: ['branch', 'shell'],
    3: ['cream', 'fan', 'map'],
    4: ['book', 'car', 'mirror'],
    5: ['pipe', 'string'],
    6: ['milk', 'newspaper', 'rose'],
}

# Define the moves
moves = [
    (4, None, 'book'),       # Remove the book from Box 4
    (4, None, 'mirror'),     # Remove the mirror from Box 4
    (3, None, 'fan'),        # Remove the fan from Box 3
    (3, None, 'map'),        # Remove the map from Box 3
    (5, None, 'pipe'),       # Remove the pipe from Box 5
    (4, None, 'car'),        # Remove the car from Box 4
    (0, None, 'shoe'),       # Remove the shoe from Box 0
    (None, 2, 'key'),        # Put the key into Box 2
    (3, None, 'cream'),      # Remove the cream from Box 3
    (None, 5, 'fig'),        # Put the fig into Box 5
    (6, 3, 'milk'),          # Move the milk from Box 6 to Box 3
    (6, 3, 'newspaper'),     # Move the newspaper from Box 6 to Box 3
    (6, 3, 'rose'),          # Move the rose from Box 6 to Box 3
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