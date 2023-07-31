# Initialize the boxes
boxes = {
    0: ['glass'],
    1: ['cash', 'guitar', 'map'],
    2: [],
    3: ['drug', 'machine', 'shell'],
    4: ['card', 'newspaper', 'tea'],
    5: ['branch', 'coat', 'rock'],
    6: ['milk', 'note', 'television'],
}

# Define the moves
moves = [
    (None, 0, 'computer'),     # Put the computer into Box 0
    (0, None, 'glass'),        # Remove the glass from Box 0
    (4, 2, 'card'),            # Move the card from Box 4 to Box 2
    (0, None, 'computer'),     # Remove the computer from Box 0
    (4, 2, 'newspaper'),       # Move the newspaper from Box 4 to Box 2
    (4, 2, 'tea'),             # Move the tea from Box 4 to Box 2
    (None, 4, 'wheel'),        # Put the wheel into Box 4
    (2, None, 'newspaper'),    # Remove the newspaper from Box 2
    (2, None, 'tea'),          # Remove the tea from Box 2
    (6, 4, 'milk'),            # Move the milk from Box 6 to Box 4
    (6, 4, 'note'),            # Move the note from Box 6 to Box 4
    (None, 0, 'ice'),          # Put the ice into Box 0
    (2, None, 'card'),         # Remove the card from Box 2
    (3, 6, 'machine'),         # Move the machine from Box 3 to Box 6
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