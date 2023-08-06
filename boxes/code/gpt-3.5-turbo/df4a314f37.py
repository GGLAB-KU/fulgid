# Initialize the boxes
boxes = {
    0: [],
    1: ['medicine'],
    2: ['beer', 'boat', 'suit'],
    3: ['pipe'],
    4: ['brain', 'newspaper', 'note'],
    5: ['plate', 'shoe'],
    6: ['bell', 'card'],
}

# Define the moves
moves = [
    (5, None, 'plate'),      # Remove the plate from Box 5
    (5, None, 'shoe'),       # Remove the shoe from Box 5
    (4, None, 'newspaper'),  # Remove the newspaper from Box 4
    (4, None, 'note'),       # Remove the note from Box 4
    (1, None, 'medicine'),   # Remove the medicine from Box 1
    (2, None, 'beer'),       # Remove the beer from Box 2
    (2, None, 'boat'),       # Remove the boat from Box 2
    (6, None, 'cream'),      # Put the cream into Box 6
    (6, None, 'cream'),      # Remove the cream from Box 6
    (None, 2, 'bomb'),       # Put the bomb into Box 2
    (None, 2, 'painting'),   # Put the painting into Box 2
    (6, None, 'bell'),       # Remove the bell from Box 6
    (4, None, 'bone'),       # Put the bone into Box 4
    (4, None, 'gift'),       # Put the gift into Box 4
    (3, None, 'pipe'),       # Remove the pipe from Box 3
    (2, 6, 'bomb'),          # Move the bomb from Box 2 to Box 6
    (2, 6, 'painting')       # Move the painting from Box 2 to Box 6
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