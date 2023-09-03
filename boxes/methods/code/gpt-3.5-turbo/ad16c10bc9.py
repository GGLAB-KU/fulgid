# Initialize the boxes
boxes = {
    0: ['ring', 'suit'],
    1: ['book', 'knife'],
    2: ['plate', 'tie'],
    3: [],
    4: ['bread', 'brick', 'cup'],
    5: ['magazine', 'shell'],
    6: ['rock', 'shirt', 'string'],
}

# Define the moves
moves = [
    (None, 2, 'crown'),       # Put the crown into Box 2
    (4, 5, 'bread'),          # Move the bread from Box 4 to Box 5
    (1, None, 'knife'),       # Remove the knife from Box 1
    (6, None, 'rock'),        # Remove the rock from Box 6
    (6, None, 'shirt'),       # Remove the shirt from Box 6
    (6, None, 'string'),      # Remove the string from Box 6
    (5, None, 'shell'),       # Remove the shell from Box 5
    (1, 5, 'book'),           # Move the book from Box 1 to Box 5
    (5, 6, 'bread'),          # Move the bread from Box 5 to Box 6
    (5, None, 'magazine'),    # Remove the magazine from Box 5
    (6, None, 'bread'),       # Remove the bread from Box 6
    (None, 5, 'game'),        # Put the game into Box 5
    (2, None, 'crown'),       # Remove the crown from Box 2
    (2, None, 'plate'),       # Remove the plate from Box 2
    (2, None, 'tie')          # Remove the tie from Box 2
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