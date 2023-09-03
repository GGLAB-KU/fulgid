# Initialize the boxes
boxes = {
    0: ['suit'],
    1: ['beer', 'cup', 'drink'],
    2: ['dress', 'string', 'tea'],
    3: ['bill', 'branch', 'fan'],
    4: ['disk', 'pot', 'radio'],
    5: ['bomb', 'engine'],
    6: ['card', 'document'],
}

# Define the moves
moves = [
    (5, None, 'engine'),       # Remove the engine from Box 5
    (2, 5, 'string'),          # Move the string from Box 2 to Box 5
    (2, 5, 'tea'),             # Move the tea from Box 2 to Box 5
    (2, None, 'dress'),        # Remove the dress from Box 2
    (None, 2, 'mirror'),       # Put the mirror into Box 2
    (1, 2, 'cup'),             # Move the cup from Box 1 to Box 2
    (1, 2, 'drink'),           # Move the drink from Box 1 to Box 2
    (None, 1, 'beer'),         # Remove the beer from Box 1
    (2, 1, 'drink'),           # Move the drink from Box 2 to Box 1
    (2, 1, 'mirror'),          # Move the mirror from Box 2 to Box 1
    (5, None, 'bomb'),         # Remove the bomb from Box 5
    (5, None, 'string'),       # Remove the string from Box 5
    (5, None, 'tea'),          # Remove the tea from Box 5
    (1, 5, 'drink'),           # Move the drink from Box 1 to Box 5
    (None, 5, 'drink'),        # Remove the drink from Box 5
    (None, 5, 'magazine'),     # Put the magazine into Box 5
    (2, None, 'cup'),          # Remove the cup from Box 2
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