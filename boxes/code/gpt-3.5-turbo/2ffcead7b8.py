# Initialize the boxes
boxes = {
    0: ['bone', 'machine', 'suit'],
    1: ['bread', 'plant'],
    2: [],
    3: ['string'],
    4: ['milk', 'radio', 'ticket'],
    5: ['dress'],
    6: ['gift'],
}

# Define the moves
moves = [
    (None, 2, 'key'),       # Put the key into Box 2
    (4, 3, 'radio'),         # Move the radio from Box 4 to Box 3
    (None, 6, 'shoe'),       # Put the shoe into Box 6
    (6, None, 'gift'),       # Remove the gift from Box 6
    (None, 2, 'letter'),     # Put the letter into Box 2
    (3, 6, 'string'),        # Move the string from Box 3 to Box 6
    (0, None, 'suit'),       # Remove the suit from Box 0
    (4, None, 'milk'),       # Remove the milk from Box 4
    (4, None, 'ticket'),     # Remove the ticket from Box 4
    (1, 6, 'bread')          # Move the bread from Box 1 to Box 6
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