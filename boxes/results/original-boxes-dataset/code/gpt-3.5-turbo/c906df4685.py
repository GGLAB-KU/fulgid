# Initialize the boxes
boxes = {
    0: ['branch', 'cream'],
    1: ['wire'],
    2: ['bowl', 'flower', 'plate'],
    3: ['bomb', 'knife'],
    4: ['coat', 'newspaper', 'pot'],
    5: ['boat', 'camera', 'cheese'],
    6: ['boot', 'chemical', 'shirt'],
}

# Define the moves
moves = [
    (4, None, 'newspaper'),     # Remove the newspaper from Box 4
    (4, None, 'pot'),           # Remove the pot from Box 4
    (5, 4, 'boat'),             # Move the boat from Box 5 to Box 4
    (5, None, 'camera'),        # Remove the camera from Box 5
    (5, None, 'cheese'),        # Remove the cheese from Box 5
    (2, None, 'bowl'),          # Remove the bowl from Box 2
    (2, None, 'flower'),        # Remove the flower from Box 2
    (2, None, 'plate'),         # Remove the plate from Box 2
    (3, None, 'bomb'),          # Remove the bomb from Box 3
    (1, None, 'wire'),          # Remove the wire from Box 1
    (3, 4, 'knife'),            # Move the knife from Box 3 to Box 4
    (6, None, 'shirt'),         # Remove the shirt from Box 6
    (6, None, 'boot'),          # Remove the boot from Box 6
    (4, 1, 'boat'),             # Move the boat from Box 4 to Box 1
    (4, 1, 'coat'),             # Move the coat from Box 4 to Box 1
    (6, 5, 'chemical'),         # Move the chemical from Box 6 to Box 5
    (0, 6, 'branch'),           # Move the branch from Box 0 to Box 6
    (0, 6, 'cream'),            # Move the cream from Box 0 to Box 6
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