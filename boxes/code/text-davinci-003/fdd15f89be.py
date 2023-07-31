# Initialize the boxes
boxes = {
    0: ['cup', 'television', 'tissue'],
    1: ['shoe'],
    2: ['cigarette', 'seed', 'tie'],
    3: ['guitar', 'key', 'ticket'],
    4: ['drug', 'mirror'],
    5: ['watch'],
    6: ['glass'],
}

# Define the moves
moves = [
    (3, None, 'key'),       # Remove the key from Box 3
    (4, 5, 'mirror'),       # Move the mirror from Box 4 to Box 5
    (3, 4, 'ticket'),       # Move the ticket from Box 3 to Box 4
    (5, 4, 'watch'),        # Move the watch from Box 5 to Box 4
    (1, None, 'shoe'),      # Remove the shoe from Box 1
    (3, 5, 'guitar'),       # Move the guitar from Box 3 to Box 5
    (6, 5, 'glass'),        # Move the glass from Box 6 to Box 5
    (5, None, 'glass'),     # Remove the glass from Box 5
    (5, None, 'guitar'),    # Remove the guitar from Box 5
    (2, None, 'cigarette'), # Remove the cigarette from Box 2
    (2, None, 'seed'),      # Remove the seed from Box 2
    (4, 1, 'drug'),         # Move the drug from Box 4 to Box 1
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