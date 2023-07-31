# Initialize the boxes
boxes = {
    0: ['ticket'],
    1: ['mirror', 'plane', 'radio'],
    2: ['bone', 'cheese', 'painting'],
    3: ['bag', 'medicine', 'pipe'],
    4: ['tape'],
    5: ['plant', 'shirt'],
    6: ['fan', 'sheet'],
}

# Define the moves
moves = [
    (1, None, 'mirror'),    # Remove the mirror from Box 1
    (1, None, 'plane'),     # Remove the plane from Box 1
    (1, None, 'radio'),     # Remove the radio from Box 1
    (None, 1, 'block'),     # Put the block into Box 1
    (None, 1, 'phone'),     # Put the phone into Box 1
    (3, 0, 'pipe'),         # Move the pipe from Box 3 to Box 0
    (5, 4, 'plant'),        # Move the plant from Box 5 to Box 4
    (5, 4, 'shirt'),        # Move the shirt from Box 5 to Box 4
    (0, 5, 'ticket'),       # Move the ticket from Box 0 to Box 5
    (3, None, 'medicine'),  # Remove the medicine from Box 3
    (None, 0, 'tie'),       # Put the tie into Box 0
    (5, 0, 'ticket'),       # Move the ticket from Box 5 to Box 0
    (1, None, 'block'),     # Remove the block from Box 1
    (1, None, 'phone'),     # Remove the phone from Box 1
    (3, None, 'bag'),       # Remove the bag from Box 3
    (0, 1, 'ticket'),       # Move the ticket from Box 0 to Box 1
    (0, 1, 'tie'),          # Move the tie from Box 0 to Box 1
    (0, None, 'pipe'),      # Remove the pipe from Box 0
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