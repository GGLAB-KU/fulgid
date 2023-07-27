# Initialize the boxes
boxes = {
    0: [],
    1: ['coat', 'drug'],
    2: ['disk', 'medicine', 'picture'],
    3: ['shell'],
    4: ['block', 'boat'],
    5: ['wire'],
    6: ['beer', 'dish', 'painting'],
}

# Define the moves
moves = [
    (None, 5, 'engine'),   # Put the engine into Box 5
    (None, 5, 'ring'),     # Put the ring into Box 5
    (3, None, 'shell'),    # Remove the shell from Box 3
    (6, None, 'beer'),     # Remove the beer from Box 6
    (6, None, 'painting'), # Remove the painting from Box 6
    (2, None, 'picture'),  # Remove the picture from Box 2
    (None, 3, 'hat'),      # Put the hat into Box 3
    (None, 3, 'paper'),    # Put the paper into Box 3
    (None, 3, 'phone'),    # Put the phone into Box 3
    (None, 0, 'boot'),     # Put the boot into Box 0
    (None, 0, 'computer'), # Put the computer into Box 0
    (3, None, 'hat'),      # Remove the hat from Box 3
    (3, None, 'paper'),    # Remove the paper from Box 3
    (3, 4, 'phone'),       # Move the phone from Box 3 to Box 4
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