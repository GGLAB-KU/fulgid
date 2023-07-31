# Initialize the boxes
boxes = {
    0: ['bone', 'computer', 'tea'],
    1: ['leaf'],
    2: [],
    3: ['bread', 'drink'],
    4: ['boat', 'tie'],
    5: ['crown'],
    6: ['flower', 'hat'],
}

# Define the moves
moves = [
    (None, 5, 'beer'),       # Put the beer into Box 5
    (None, 5, 'radio'),      # Put the radio into Box 5
    (3, 6, 'drink'),         # Move the drink from Box 3 to Box 6
    (5, None, 'crown'),      # Remove the crown from Box 5
    (5, None, 'radio'),      # Remove the radio from Box 5
    (None, 5, 'cross'),      # Put the cross into Box 5
    (1, 5, 'leaf'),          # Move the leaf from Box 1 to Box 5
    (5, None, 'beer'),       # Remove the beer from Box 5
    (None, 5, 'apple'),      # Put the apple into Box 5
    (None, 3, 'coat'),       # Put the coat into Box 3
    (None, 3, 'note'),       # Put the note into Box 3
    (5, 1, 'cross'),         # Move the cross from Box 5 to Box 1
    (5, 1, 'leaf'),          # Move the leaf from Box 5 to Box 1
    (None, 1, 'newspaper'),  # Put the newspaper into Box 1
    (1, None, 'newspaper')   # Remove the newspaper from Box 1
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