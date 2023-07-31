# Initialize the boxes
boxes = {
    0: ['bottle'],
    1: ['pipe'],
    2: ['dish', 'game'],
    3: [],
    4: ['plate'],
    5: ['car', 'painting', 'plant'],
    6: ['milk'],
}

# Define the moves
moves = [
    (None, 2, 'picture'),    # Put the picture into Box 2
    (2, None, 'picture'),    # Remove the picture from Box 2
    (2, 1, 'dish'),          # Move the dish from Box 2 to Box 1
    (2, 1, 'game'),          # Move the game from Box 2 to Box 1
    (1, None, 'dish'),       # Remove the dish from Box 1
    (1, None, 'game'),       # Remove the game from Box 1
    (0, 4, 'bottle'),        # Move the bottle from Box 0 to Box 4
    (5, None, 'plant'),      # Remove the plant from Box 5
    (None, 5, 'engine'),     # Put the engine into Box 5
    (5, None, 'car'),        # Remove the car from Box 5
    (None, 0, 'coffee'),     # Put the coffee into Box 0
    (None, 0, 'medicine'),   # Put the medicine into Box 0
    (6, None, 'milk'),       # Remove the milk from Box 6
    (5, None, 'engine')      # Remove the engine from Box 5
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