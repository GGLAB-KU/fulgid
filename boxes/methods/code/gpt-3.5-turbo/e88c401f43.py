# Initialize the boxes
boxes = {
    0: ['meat'],
    1: ['cigarette', 'rock'],
    2: ['bus', 'milk', 'picture'],
    3: ['boat'],
    4: ['car', 'fish', 'string'],
    5: [],
    6: ['pipe', 'radio'],
}

# Define the moves
moves = [
    (0, None, 'meat'),          # Remove the meat from Box 0
    (4, None, 'string'),        # Remove the string from Box 4
    (3, None, 'boat'),          # Remove the boat from Box 3
    (6, None, 'pipe'),          # Remove the pipe from Box 6
    (6, None, 'radio'),         # Remove the radio from Box 6
    (1, 3, 'rock'),             # Move the rock from Box 1 to Box 3
    (1, None, 'cigarette'),     # Remove the cigarette from Box 1
    (None, 6, 'apple'),         # Put the apple into Box 6
    (None, 6, 'creature'),      # Put the creature into Box 6
    (None, 6, 'plate'),         # Put the plate into Box 6
    (3, 1, 'rock'),             # Move the rock from Box 3 to Box 1
    (None, 1, 'drink'),         # Put the drink into Box 1
    (None, 1, 'glass'),         # Put the glass into Box 1
    (6, None, 'apple'),         # Remove the apple from Box 6
    (3, None, 'card'),          # Put the card into Box 3
    (None, 5, 'dish')           # Put the dish into Box 5
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