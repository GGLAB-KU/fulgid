# Initialize the boxes
boxes = {
    0: [],
    1: ['card', 'milk', 'painting'],
    2: ['book', 'cake', 'guitar'],
    3: ['chemical'],
    4: ['letter', 'ticket'],
    5: ['camera', 'gift', 'pot'],
    6: ['coffee', 'drink', 'tie'],
}

# Define the moves
moves = [
    (3, None, 'chemical'),     # Remove the chemical from Box 3
    (4, None, 'ticket'),       # Remove the ticket from Box 4
    (6, None, 'drink'),        # Remove the drink from Box 6
    (6, None, 'coffee'),       # Remove the coffee from Box 6
    (None, 6, 'branch'),       # Put the branch into Box 6
    (None, 6, 'tissue'),       # Put the tissue into Box 6
    (1, None, 'card'),         # Remove the card from Box 1
    (1, None, 'milk'),         # Remove the milk from Box 1
    (2, None, 'cake'),         # Remove the cake from Box 2
    (6, None, 'branch'),       # Remove the branch from Box 6
    (6, None, 'tie'),          # Remove the tie from Box 6
    (6, None, 'tissue'),       # Remove the tissue from Box 6
    (1, None, 'painting'),     # Remove the painting from Box 1
    (5, None, 'gift'),         # Remove the gift from Box 5
    (5, None, 'pot'),          # Remove the pot from Box 5
    (None, 4, 'gift'),         # Put the gift into Box 4
    (None, 6, 'crown')         # Put the crown into Box 6
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