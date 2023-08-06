# Initialize the boxes
boxes = {
    0: ['gift'],
    1: ['apple', 'phone', 'plane'],
    2: ['machine', 'ticket'],
    3: ['fan', 'string', 'wire'],
    4: ['television', 'tie'],
    5: ['note'],
    6: ['boat', 'glass', 'milk'],
}

# Define the moves
moves = [
    (5, 2, 'note'),         # Move the note from Box 5 to Box 2
    (3, None, 'fan'),       # Remove the fan from Box 3
    (3, None, 'string'),    # Remove the string from Box 3
    (3, None, 'wire'),      # Remove the wire from Box 3
    (0, 4, 'gift'),         # Move the gift from Box 0 to Box 4
    (4, 0, 'gift'),         # Move the gift from Box 4 to Box 0
    (4, None, 'television'), # Remove the television from Box 4
    (6, 3, 'glass'),        # Move the glass from Box 6 to Box 3
    (6, 3, 'milk'),         # Move the milk from Box 6 to Box 3
    (2, None, 'note'),      # Remove the note from Box 2
    (None, 4, 'knife'),     # Put the knife into Box 4
    (None, 4, 'map'),       # Put the map into Box 4
    (None, 4, 'pipe'),      # Put the pipe into Box 4
    (4, 5, 'map'),          # Move the map from Box 4 to Box 5
    (4, 5, 'knife'),        # Move the knife from Box 4 to Box 5
    (6, 5, 'boat'),         # Move the boat from Box 6 to Box 5
    (None, 6, 'bill')       # Put the bill into Box 6
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