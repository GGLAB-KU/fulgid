# Initialize the boxes
boxes = {
    0: ['cigarette', 'pipe'],
    1: ['book', 'magazine', 'stone'],
    2: ['flower'],
    3: ['medicine', 'paper', 'rock'],
    4: ['block'],
    5: [],
    6: ['cake', 'engine'],
}

# Define the moves
moves = [
    (None, 2, 'computer'),   # Put the computer into Box 2
    (4, 2, 'block'),         # Move the block from Box 4 to Box 2
    (2, 6, 'block'),         # Move the block from Box 2 to Box 6
    (3, None, 'medicine'),   # Remove the medicine from Box 3
    (3, None, 'paper'),      # Remove the paper from Box 3
    (3, None, 'rock'),       # Remove the rock from Box 3
    (None, 5, 'bill'),       # Put the bill into Box 5
    (None, 5, 'brick'),      # Put the brick into Box 5
    (None, 5, 'cream'),      # Put the cream into Box 5
    (1, 2, 'stone'),         # Move the stone from Box 1 to Box 2
    (None, 4, 'bread')       # Put the bread into Box 4
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