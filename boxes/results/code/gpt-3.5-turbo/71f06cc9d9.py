# Initialize the boxes
boxes = {
    0: ['bone'],
    1: ['suit'],
    2: ['cake', 'letter', 'medicine'],
    3: [],
    4: ['game', 'gift', 'hat'],
    5: ['bell', 'boat', 'knife'],
    6: ['car', 'cigarette', 'disk'],
}

# Define the moves
moves = [
    (5, None, 'bell'),       # Remove the bell from Box 5
    (5, None, 'knife'),      # Remove the knife from Box 5
    (1, None, 'suit'),       # Remove the suit from Box 1
    (2, 1, 'cake'),          # Move the cake from Box 2 to Box 1
    (2, 1, 'letter'),        # Move the letter from Box 2 to Box 1
    (0, None, 'drug'),       # Put the drug into Box 0
    (0, None, 'rock'),       # Put the rock into Box 0
    (2, None, 'medicine')    # Remove the medicine from Box 2
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