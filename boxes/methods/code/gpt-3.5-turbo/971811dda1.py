# Initialize the boxes
boxes = {
    0: ['bell', 'boat', 'bus'],
    1: ['branch', 'brick', 'television'],
    2: ['card', 'fan', 'wire'],
    3: ['book'],
    4: ['ice'],
    5: [],
    6: ['drug', 'rose'],
}

# Define the moves
moves = [
    (0, None, 'boat'),       # Remove the boat from Box 0
    (6, None, 'drug'),       # Remove the drug from Box 6
    (6, None, 'rose'),       # Remove the rose from Box 6
    (2, None, 'card'),       # Remove the card from Box 2
    (0, 6, 'bell'),          # Move the bell from Box 0 to Box 6
    (0, 6, 'bus'),           # Move the bus from Box 0 to Box 6
    (4, None, 'ice'),        # Remove the ice from Box 4
    (None, 0, 'paper'),      # Put the paper into Box 0
    (None, 0, 'tea'),        # Put the tea into Box 0
    (None, 0, 'note'),       # Put the note into Box 0
    (0, None, 'note'),       # Remove the note from Box 0
    (0, None, 'paper'),      # Remove the paper from Box 0
    (6, 0, 'bell'),          # Move the bell from Box 6 to Box 0
    (0, None, 'bell'),       # Remove the bell from Box 0
    (6, None, 'bus'),        # Remove the bus from Box 6
    (None, 6, 'brain'),      # Put the brain into Box 6
    (None, 6, 'note')        # Put the note into Box 6
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