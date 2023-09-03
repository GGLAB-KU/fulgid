# Initialize the boxes
boxes = {
    0: ['leaf', 'map'],
    1: ['cake'],
    2: [],
    3: ['cash', 'gift'],
    4: ['note', 'paper', 'shoe'],
    5: ['bomb', 'branch', 'plate'],
    6: ['game'],
}

# Define the moves
moves = [
    (0, None, 'leaf'),       # Remove the leaf from Box 0
    (0, None, 'map'),        # Remove the map from Box 0
    (4, 0, 'shoe'),          # Move the shoe from Box 4 to Box 0
    (None, 1, 'newspaper'),  # Put the newspaper into Box 1
    (1, 2, 'cake'),          # Move the cake from Box 1 to Box 2
    (1, 2, 'newspaper'),     # Move the newspaper from Box 1 to Box 2
    (None, 3, 'fish'),       # Put the fish into Box 3
    (4, 0, 'note'),          # Move the note from Box 4 to Box 0
    (4, None, 'paper'),      # Remove the paper from Box 4
    (5, None, 'branch'),     # Remove the branch from Box 5
    (2, 5, 'newspaper'),     # Move the newspaper from Box 2 to Box 5
    (5, 4, 'bomb'),          # Move the bomb from Box 5 to Box 4
    (5, 4, 'newspaper'),     # Move the newspaper from Box 5 to Box 4
    (5, 4, 'plate'),         # Move the plate from Box 5 to Box 4
    (3, 5, 'fish'),          # Move the fish from Box 3 to Box 5
    (5, 2, 'fish'),          # Move the fish from Box 5 to Box 2
    (2, 5, 'cake'),          # Move the cake from Box 2 to Box 5
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