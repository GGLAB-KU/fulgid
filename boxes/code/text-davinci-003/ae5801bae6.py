# Initialize the boxes
boxes = {
    0: ['bomb'],
    1: [],
    2: [],
    3: ['flower', 'gift', 'guitar'],
    4: ['drink'],
    5: ['newspaper', 'painting', 'radio'],
    6: ['dish'],
}

# Define the moves
moves = [
    (3, None, 'flower'),    # Remove the flower from Box 3
    (3, None, 'guitar'),    # Remove the guitar from Box 3
    (4, None, 'drink'),     # Remove the drink from Box 4
    (5, None, 'newspaper'), # Remove the newspaper from Box 5
    (3, 1, 'gift'),         # Move the gift from Box 3 to Box 1
    (5, None, 'radio'),     # Remove the radio from Box 5
    (5, None, 'painting'),  # Remove the painting from Box 5
    (6, None, 'dish'),      # Remove the dish from Box 6
    (None, 5, 'note'),      # Put the note into Box 5
    (None, 5, 'seed'),      # Put the seed into Box 5
    (1, 4, 'gift'),         # Move the gift from Box 1 to Box 4
    (None, 6, 'string'),    # Put the string into Box 6
    (6, None, 'string')     # Remove the string from Box 6
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