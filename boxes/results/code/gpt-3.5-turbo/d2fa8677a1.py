# Initialize the boxes
boxes = {
    0: ['fish'],
    1: ['newspaper', 'painting'],
    2: ['bag', 'coffee'],
    3: ['bone', 'clock', 'phone'],
    4: ['crown', 'seed'],
    5: ['creature', 'flower', 'ticket'],
    6: ['apple', 'bowl', 'plane'],
}

# Define the moves
moves = [
    (None, 0, 'bomb'),       # Put the bomb into Box 0
    (None, 0, 'ring'),       # Put the ring into Box 0
    (4, None, 'crown'),      # Remove the crown from Box 4
    (4, None, 'seed'),       # Remove the seed from Box 4
    (5, None, 'creature'),   # Remove the creature from Box 5
    (5, None, 'flower'),     # Remove the flower from Box 5
    (0, None, 'fish'),       # Remove the fish from Box 0
    (None, 4, 'milk'),       # Put the milk into Box 4
    (0, 4, 'bomb'),          # Move the bomb from Box 0 to Box 4
    (5, 1, 'ticket'),        # Move the ticket from Box 5 to Box 1
    (1, 5, 'ticket'),        # Move the ticket from Box 1 to Box 5
    (1, 0, 'newspaper'),     # Move the newspaper from Box 1 to Box 0
    (1, 0, 'painting'),      # Move the painting from Box 1 to Box 0
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