# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['file', 'map', 'ticket'],
    3: ['bag', 'drug', 'flower'],
    4: ['wheel'],
    5: ['picture', 'plate', 'stone'],
    6: ['dish', 'phone'],
}

# Define the moves
moves = [
    (6, None, 'dish'),       # Remove the dish from Box 6
    (5, 1, 'picture'),       # Move the picture from Box 5 to Box 1
    (5, 1, 'plate'),         # Move the plate from Box 5 to Box 1
    (5, 1, 'stone'),         # Move the stone from Box 5 to Box 1
    (4, None, 'wheel'),      # Remove the wheel from Box 4
    (None, 5, 'cigarette'),  # Put the cigarette into Box 5
    (None, 5, 'note'),       # Put the note into Box 5
    (5, 6, 'note'),          # Move the note from Box 5 to Box 6
    (None, 5, 'radio'),      # Put the radio into Box 5
    (6, None, 'note'),       # Remove the note from Box 6
    (6, None, 'phone'),      # Remove the phone from Box 6
    (5, None, 'radio'),      # Remove the radio from Box 5
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