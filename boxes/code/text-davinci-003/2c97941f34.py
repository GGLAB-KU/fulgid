# Initialize the boxes
boxes = {
    0: [],
    1: ['ice', 'key'],
    2: ['disk', 'tape', 'tie'],
    3: ['knife', 'television', 'tissue'],
    4: ['cigarette'],
    5: ['boat', 'dish', 'shell'],
    6: ['meat', 'phone', 'wheel'],
}

# Define the moves
moves = [
    (1, None, 'ice'),       # Remove the ice from Box 1
    (None, 0, 'cheese'),    # Put the cheese into Box 0
    (5, None, 'boat'),      # Remove the boat from Box 5
    (1, None, 'key'),       # Remove the key from Box 1
    (5, None, 'dish'),      # Remove the dish from Box 5
    (5, None, 'shell'),     # Remove the shell from Box 5
    (0, None, 'cheese'),    # Remove the cheese from Box 0
    (3, None, 'knife'),     # Remove the knife from Box 3
    (4, 0, 'cigarette'),    # Move the cigarette from Box 4 to Box 0
    (None, 5, 'clock'),     # Put the clock into Box 5
    (None, 5, 'train'),     # Put the train into Box 5
    (5, 1, 'train'),        # Move the train from Box 5 to Box 1
    (0, None, 'cigarette'), # Remove the cigarette from Box 0
    (6, None, 'meat'),      # Remove the meat from Box 6
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