# Initialize the boxes
boxes = {
    0: ['note'],
    1: ['boat', 'branch', 'television'],
    2: ['computer', 'picture'],
    3: [],
    4: ['cup'],
    5: ['bag', 'beer', 'milk'],
    6: ['hat', 'watch'],
}

# Define the moves
moves = [
    (4, 0, 'cup'),       # Move the cup from Box 4 to Box 0
    (0, None, 'note'),   # Remove the note from Box 0
    (None, 6, 'ball'),   # Put the ball into Box 6
    (2, 0, 'picture'),   # Move the picture from Box 2 to Box 0
    (None, 4, 'cream'),  # Put the cream into Box 4
    (1, None, 'branch'), # Remove the branch from Box 1
    (5, None, 'beer')    # Remove the beer from Box 5
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