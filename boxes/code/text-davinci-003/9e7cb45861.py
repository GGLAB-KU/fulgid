# Initialize the boxes
boxes = {
    0: ['cake', 'painting'],
    1: ['knife'],
    2: ['bus', 'cheese', 'seed'],
    3: ['letter'],
    4: ['ticket'],
    5: ['medicine'],
    6: ['crown', 'phone'],
}

# Define the moves
moves = [
    (0, 1, 'painting'),     # Move the painting from Box 0 to Box 1
    (4, 3, 'ticket'),       # Move the ticket from Box 4 to Box 3
    (6, None, 'phone'),     # Remove the phone from Box 6
    (6, None, 'crown'),     # Remove the crown from Box 6
    (None, 5, 'dish'),      # Put the dish into Box 5
    (0, 6, 'cake'),         # Move the cake from Box 0 to Box 6
    (6, None, 'cake'),      # Remove the cake from Box 6
    (1, 5, 'knife'),        # Move the knife from Box 1 to Box 5
    (5, 6, 'dish'),         # Move the dish from Box 5 to Box 6
    (5, 6, 'medicine'),     # Move the medicine from Box 5 to Box 6
    (5, 4, 'knife'),        # Move the knife from Box 5 to Box 4
    (None, 0, 'bread'),     # Put the bread into Box 0
    (None, 0, 'flower'),    # Put the flower into Box 0
    (2, 4, 'bus'),          # Move the bus from Box 2 to Box 4
    (2, 4, 'seed')          # Move the seed from Box 2 to Box 4
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