# Initialize the boxes
boxes = {
    0: ['ticket'],
    1: ['brick', 'glass', 'tea'],
    2: ['beer', 'painting', 'radio'],
    3: ['bus'],
    4: ['clock'],
    5: ['disk', 'medicine'],
    6: ['book', 'mirror', 'stone'],
}

# Define the moves
moves = [
    (0, None, 'ticket'),     # Remove the ticket from Box 0
    (None, 5, 'drug'),       # Put the drug into Box 5
    (1, None, 'brick'),      # Remove the brick from Box 1
    (1, None, 'glass'),      # Remove the glass from Box 1
    (1, None, 'tea'),        # Remove the tea from Box 1
    (6, None, 'stone'),      # Remove the stone from Box 6
    (5, 4, 'drug'),          # Move the drug from Box 5 to Box 4
    (5, 4, 'medicine'),      # Move the medicine from Box 5 to Box 4
    (4, None, 'drug'),       # Remove the drug from Box 4
    (4, None, 'medicine'),   # Remove the medicine from Box 4
    (2, None, 'beer'),       # Remove the beer from Box 2
    (2, None, 'painting'),   # Remove the painting from Box 2
    (2, None, 'radio'),      # Remove the radio from Box 2
    (6, None, 'book'),       # Remove the book from Box 6
    (6, 0, 'mirror'),        # Move the mirror from Box 6 to Box 0
    (0, 3, 'mirror'),        # Move the mirror from Box 0 to Box 3
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