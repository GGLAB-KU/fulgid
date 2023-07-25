# Initialize the boxes
boxes = {
    0: ['cash', 'ticket'],
    1: [],
    2: ['beer', 'brain', 'guitar'],
    3: ['medicine', 'newspaper'],
    4: ['crown'],
    5: ['ice', 'painting'],
    6: ['bomb', 'boot', 'plane'],
}

# Define the moves
moves = [
    (None, 5, 'meat'),       # Put the meat into Box 5
    (0, 1, 'ticket'),        # Move the ticket from Box 0 to Box 1
    (3, None, 'newspaper'),  # Remove the newspaper from Box 3
    (2, None, 'guitar'),     # Remove the guitar from Box 2
    (2, None, 'brain'),      # Remove the brain from Box 2
    (2, None, 'beer'),       # Remove the beer from Box 2
    (1, 3, 'ticket'),        # Move the ticket from Box 1 to Box 3
    (3, 2, 'medicine'),      # Move the medicine from Box 3 to Box 2
    (0, 3, 'cash'),          # Move the cash from Box 0 to Box 3
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