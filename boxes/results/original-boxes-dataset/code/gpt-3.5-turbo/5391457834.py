# Initialize the boxes
boxes = {
    0: [],
    1: ['cash', 'hat'],
    2: ['car', 'phone', 'sheet'],
    3: ['crown'],
    4: ['document', 'medicine'],
    5: ['jacket', 'machine', 'tape'],
    6: ['cream'],
}

# Define the moves
moves = [
    (2, None, 'car'),       # Remove the car from Box 2
    (2, None, 'sheet'),     # Remove the sheet from Box 2
    (None, 4, 'picture'),   # Put the picture into Box 4
    (None, 3, 'boat'),      # Put the boat into Box 3
    (6, 1, 'cream'),        # Move the cream from Box 6 to Box 1
    (2, 6, 'phone'),        # Move the phone from Box 2 to Box 6
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