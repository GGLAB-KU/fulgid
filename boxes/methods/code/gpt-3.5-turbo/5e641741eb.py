# Initialize the boxes
boxes = {
    0: ['beer', 'gift'],
    1: ['boat', 'crown', 'jacket'],
    2: ['ice', 'meat'],
    3: ['bread'],
    4: ['dress', 'tea', 'ticket'],
    5: ['cup', 'milk'],
    6: ['drug', 'magazine', 'pot'],
}

# Define the moves
moves = [
    (6, None, 'magazine'),     # Remove the magazine from Box 6
    (6, None, 'pot'),          # Remove the pot from Box 6
    (3, 5, 'bread'),           # Move the bread from Box 3 to Box 5
    (4, None, 'dress'),        # Remove the dress from Box 4
    (None, 0, 'plate'),        # Put the plate into Box 0
    (2, None, 'ice'),          # Remove the ice from Box 2
    (2, None, 'meat'),         # Remove the meat from Box 2
    (4, 2, 'ticket'),          # Move the ticket from Box 4 to Box 2
    (None, 3, 'chemical'),     # Put the chemical into Box 3
    (None, 3, 'seed'),         # Put the seed into Box 3
    (5, None, 'cup'),          # Remove the cup from Box 5
    (None, 6, 'bill')          # Put the bill into Box 6
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