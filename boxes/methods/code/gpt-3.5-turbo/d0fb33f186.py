# Initialize the boxes
boxes = {
    0: ['beer'],
    1: ['cake', 'gift', 'letter'],
    2: ['hat', 'medicine'],
    3: ['bill', 'fan', 'picture'],
    4: ['apple', 'milk', 'newspaper'],
    5: ['bomb', 'clock'],
    6: ['fig', 'leaf'],
}

# Define the moves
moves = [
    (3, None, 'fan'),       # Remove the fan from Box 3
    (3, None, 'picture'),   # Remove the picture from Box 3
    (None, 3, 'rock'),      # Put the rock into Box 3
    (6, None, 'fig'),       # Remove the fig from Box 6
    (None, 0, 'glass'),     # Put the glass into Box 0
    (2, 6, 'medicine'),     # Move the medicine from Box 2 to Box 6
    (2, 3, 'hat'),          # Move the hat from Box 2 to Box 3
    (None, 2, 'boot'),      # Put the boot into Box 2
    (None, 2, 'fig'),       # Put the fig into Box 2
    (None, 2, 'shoe'),      # Put the shoe into Box 2
    (None, 6, 'painting'),  # Put the painting into Box 6
    (2, 0, 'boot'),         # Move the boot from Box 2 to Box 0
    (6, None, 'painting'),  # Remove the painting from Box 6
    (4, 6, 'newspaper'),    # Move the newspaper from Box 4 to Box 6
    (6, None, 'leaf'),      # Remove the leaf from Box 6
    (6, None, 'medicine')   # Remove the medicine from Box 6
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