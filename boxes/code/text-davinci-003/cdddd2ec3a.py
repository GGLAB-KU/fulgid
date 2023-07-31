# Initialize the boxes
boxes = {
    0: ['plant', 'sheet'],
    1: ['coffee', 'leaf', 'stone'],
    2: [],
    3: ['fish'],
    4: ['bomb', 'cross', 'key'],
    5: ['card', 'ticket'],
    6: ['tie'],
}

# Define the moves
moves = [
    (6, None, 'tie'),       # Remove the tie from Box 6
    (None, 6, 'plane'),     # Put the plane into Box 6
    (6, None, 'plane'),     # Remove the plane from Box 6
    (3, None, 'fish'),      # Remove the fish from Box 3
    (1, 0, 'stone'),        # Move the stone from Box 1 to Box 0
    (None, 6, 'boat'),      # Put the boat into Box 6
    (None, 6, 'letter'),    # Put the letter into Box 6
    (4, 1, 'cross'),        # Move the cross from Box 4 to Box 1
    (6, 3, 'boat'),         # Move the boat from Box 6 to Box 3
    (6, 3, 'letter'),       # Move the letter from Box 6 to Box 3
    (0, 4, 'plant'),        # Move the plant from Box 0 to Box 4
    (1, 6, 'cross'),        # Move the cross from Box 1 to Box 6
    (6, 5, 'cross'),        # Move the cross from Box 6 to Box 5
    (5, None, 'cross'),     # Remove the cross from Box 5
    (5, None, 'ticket')     # Remove the ticket from Box 5
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