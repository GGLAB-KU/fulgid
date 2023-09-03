# Initialize the boxes
boxes = {
    0: ['fish', 'paper'],
    1: ['chemical', 'painting'],
    2: [],
    3: ['beer', 'map', 'sheet'],
    4: ['bomb', 'cream', 'plane'],
    5: ['gift'],
    6: ['clock', 'meat'],
}

# Define the moves
moves = [
    (None, 2, 'bill'),       # Put the bill into Box 2
    (None, 2, 'coat'),       # Put the coat into Box 2
    (5, 6, 'gift'),          # Move the gift from Box 5 to Box 6
    (1, None, 'chemical'),   # Remove the chemical from Box 1
    (4, None, 'bomb'),       # Remove the bomb from Box 4
    (0, 5, 'fish'),          # Move the fish from Box 0 to Box 5
    (0, 5, 'paper'),         # Move the paper from Box 0 to Box 5
    (5, 4, 'fish'),          # Move the fish from Box 5 to Box 4
    (5, None, 'paper')       # Remove the paper from Box 5
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