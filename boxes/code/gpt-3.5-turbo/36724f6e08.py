# Initialize the boxes
boxes = {
    0: ['camera', 'note', 'suit'],
    1: ['bell'],
    2: ['ice', 'mirror'],
    3: [],
    4: ['bottle'],
    5: ['game', 'painting', 'pipe'],
    6: ['brain', 'tissue'],
}

# Define the moves
moves = [
    (None, 6, 'drink'),         # Put the drink into Box 6
    (5, 3, 'painting'),         # Move the painting from Box 5 to Box 3
    (1, 4, 'bell'),             # Move the bell from Box 1 to Box 4
    (3, 5, 'painting'),         # Move the painting from Box 3 to Box 5
    (5, None, 'game'),          # Remove the game from Box 5
    (5, None, 'painting'),      # Remove the painting from Box 5
    (5, None, 'pipe'),          # Remove the pipe from Box 5
    (4, 5, 'bottle'),           # Move the bottle from Box 4 to Box 5
    (5, None, 'bottle'),        # Remove the bottle from Box 5
    (2, 5, 'ice'),              # Move the ice from Box 2 to Box 5
    (2, 5, 'mirror'),           # Move the mirror from Box 2 to Box 5
    (None, 4, 'knife'),         # Put the knife into Box 4
    (5, None, 'ice'),           # Remove the ice from Box 5
    (5, None, 'mirror'),        # Remove the mirror from Box 5
    (None, 3, 'computer'),      # Put the computer into Box 3
    (None, 3, 'medicine')       # Put the medicine into Box 3
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