# Initialize the boxes
boxes = {
    0: ['ball', 'tape', 'television'],
    1: ['clock', 'cross'],
    2: ['paper', 'rose'],
    3: ['key'],
    4: ['drug', 'tea'],
    5: ['branch', 'card'],
    6: ['gift'],
}

# Define the moves
moves = [
    (6, 5, 'gift'),         # Move the gift from Box 6 to Box 5
    (5, 3, 'card'),         # Move the card from Box 5 to Box 3
    (5, 3, 'gift'),         # Move the gift from Box 5 to Box 3
    (1, 5, 'clock'),        # Move the clock from Box 1 to Box 5
    (3, 4, 'card'),         # Move the card from Box 3 to Box 4
    (0, None, 'tape'),      # Remove the tape from Box 0
    (5, 6, 'branch'),       # Move the branch from Box 5 to Box 6
    (5, 6, 'clock'),        # Move the clock from Box 5 to Box 6
    (4, None, 'card'),      # Remove the card from Box 4
    (4, None, 'tea'),       # Remove the tea from Box 4
    (3, None, 'gift'),      # Remove the gift from Box 3
    (None, 1, 'boat'),      # Put the boat into Box 1
    (3, 2, 'key'),          # Move the key from Box 3 to Box 2
    (4, 1, 'drug'),         # Move the drug from Box 4 to Box 1
    (None, 4, 'cash'),      # Put the cash into Box 4
    (None, 4, 'tea')        # Put the tea into Box 4
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