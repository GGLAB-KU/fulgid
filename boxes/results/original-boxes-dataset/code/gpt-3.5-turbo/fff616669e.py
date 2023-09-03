# Initialize the boxes
boxes = {
    0: ['bread', 'document', 'wheel'],
    1: ['cash'],
    2: ['drink'],
    3: ['cigarette'],
    4: ['ice', 'shirt', 'television'],
    5: ['bottle', 'brick', 'tape'],
    6: ['file'],
}

# Define the moves
moves = [
    (1, None, 'cash'),       # Remove the cash from Box 1
    (6, None, 'file'),       # Remove the file from Box 6
    (None, 1, 'hat'),        # Put the hat into Box 1
    (None, 1, 'phone'),      # Put the phone into Box 1
    (None, 3, 'picture'),    # Put the picture into Box 3
    (None, 1, 'boot'),       # Put the boot into Box 1
    (1, 2, 'hat'),           # Move the hat from Box 1 to Box 2
    (1, 2, 'phone'),         # Move the phone from Box 1 to Box 2
    (3, 1, 'cigarette'),     # Move the cigarette from Box 3 to Box 1
    (3, 1, 'picture'),       # Move the picture from Box 3 to Box 1
    (1, None, 'picture')     # Remove the picture from Box 1
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