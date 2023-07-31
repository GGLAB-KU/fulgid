# Initialize the boxes
boxes = {
    0: ['egg', 'tea'],
    1: ['painting', 'phone', 'watch'],
    2: ['string'],
    3: ['car', 'medicine', 'paper'],
    4: ['ice'],
    5: ['boat'],
    6: [],
}

# Define the moves
moves = [
    (1, None, 'watch'),     # Remove the watch from Box 1
    (2, None, 'string'),    # Remove the string from Box 2
    (1, None, 'painting'),  # Remove the painting from Box 1
    (1, None, 'phone'),     # Remove the phone from Box 1
    (None, 4, 'pot'),       # Put the pot into Box 4
    (4, None, 'ice'),       # Remove the ice from Box 4
    (4, None, 'pot'),       # Remove the pot from Box 4
    (None, 1, 'suit'),      # Put the suit into Box 1
    (0, None, 'tea'),       # Remove the tea from Box 0
    (None, 1, 'pot'),       # Put the pot into Box 1
    (0, None, 'egg'),       # Remove the egg from Box 0
    (3, 1, 'medicine'),     # Move the medicine from Box 3 to Box 1
    (None, 2, 'meat'),      # Put the meat into Box 2
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