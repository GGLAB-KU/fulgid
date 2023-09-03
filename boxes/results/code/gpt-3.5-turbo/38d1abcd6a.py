# Initialize the boxes
boxes = {
    0: ['shirt', 'watch', 'wheel'],
    1: ['drink', 'fish', 'machine'],
    2: ['bread', 'crown', 'guitar'],
    3: ['string'],
    4: ['bag', 'game', 'television'],
    5: ['computer', 'gift', 'shell'],
    6: ['bottle', 'pot'],
}

# Define the moves
moves = [
    (3, None, 'string'),       # Remove the string from Box 3
    (0, None, 'shirt'),        # Remove the shirt from Box 0
    (0, None, 'wheel'),        # Remove the wheel from Box 0
    (None, 0, 'card'),         # Put the card into Box 0
    (0, 3, 'watch'),           # Move the watch from Box 0 to Box 3
    (5, 0, 'shell'),           # Move the shell from Box 5 to Box 0
    (3, None, 'watch'),        # Remove the watch from Box 3
    (1, None, 'fish'),         # Remove the fish from Box 1
    (1, None, 'machine'),      # Remove the machine from Box 1
    (1, 6, 'drink'),           # Move the drink from Box 1 to Box 6
    (None, 0, 'mirror'),       # Put the mirror into Box 0
    (0, None, 'card'),         # Remove the card from Box 0
    (None, 1, 'chemical'),     # Put the chemical into Box 1
    (4, None, 'bag')           # Remove the bag from Box 4
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