# Initialize the boxes
boxes = {
    0: ['phone'],
    1: ['cake'],
    2: ['bone'],
    3: ['car', 'drink', 'machine'],
    4: ['cheese', 'ice', 'medicine'],
    5: ['bag', 'dress', 'plant'],
    6: [],
}

# Define the moves
moves = [
    (None, 3, 'phone'),     # Put the phone into Box 3
    (None, 3, 'cake'),      # Put the cake into Box 3
    (None, 3, 'bone'),      # Put the bone into Box 3
    (None, 3, 'car'),       # Put the car into Box 3
    (None, 3, 'drink'),     # Put the drink into Box 3
    (None, 3, 'machine'),   # Put the machine into Box 3
    (None, 4, 'cheese'),    # Put the cheese into Box 4
    (None, 4, 'ice'),       # Put the ice into Box 4
    (None, 4, 'medicine'),  # Put the medicine into Box 4
    (None, 5, 'bag'),       # Put the bag into Box 5
    (None, 5, 'dress'),     # Put the dress into Box 5
    (None, 5, 'plant'),     # Put the plant into Box 5
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