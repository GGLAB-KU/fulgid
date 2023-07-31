# Initialize the boxes
boxes = {
    0: ['brain', 'coffee'],
    1: ['fish'],
    2: ['bag', 'guitar', 'paper'],
    3: ['car', 'meat'],
    4: ['gift', 'mirror'],
    5: ['card'],
    6: ['cream', 'crown', 'key'],
}

# Define the moves
moves = [
    (1, 0, 'fish'),         # Move the fish from Box 1 to Box 0
    (6, None, 'crown'),     # Remove the crown from Box 6
    (6, None, 'key'),       # Remove the key from Box 6
    (None, 5, 'phone'),     # Put the phone into Box 5
    (None, 5, 'plate'),     # Put the plate into Box 5
    (5, None, 'phone'),     # Remove the phone from Box 5
    (0, 3, 'coffee'),       # Move the coffee from Box 0 to Box 3
    (None, 1, 'leaf'),      # Put the leaf into Box 1
    (2, None, 'guitar'),    # Remove the guitar from Box 2
    (4, 2, 'gift'),         # Move the gift from Box 4 to Box 2
    (6, 5, 'cream'),        # Move the cream from Box 6 to Box 5
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