# Initialize the boxes
boxes = {
    0: ['ticket'],
    1: ['cup', 'watch'],
    2: ['fish', 'leaf', 'newspaper'],
    3: ['coffee'],
    4: ['camera', 'glass', 'milk'],
    5: ['chemical', 'letter'],
    6: ['bill', 'brain', 'pipe'],
}

# Define the moves
moves = [
    (None, 1, 'boot'),       # Put the boot into Box 1
    (6, None, 'bill'),       # Remove the bill from Box 6
    (6, None, 'brain'),      # Remove the brain from Box 6
    (6, None, 'pipe'),       # Remove the pipe from Box 6
    (3, 6, 'coffee'),        # Move the coffee from Box 3 to Box 6
    (2, 0, 'newspaper'),     # Move the newspaper from Box 2 to Box 0
    (5, None, 'chemical'),   # Remove the chemical from Box 5
    (5, None, 'letter'),     # Remove the letter from Box 5
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