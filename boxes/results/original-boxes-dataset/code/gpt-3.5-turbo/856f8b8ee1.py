# Initialize the boxes
boxes = {
    0: ['bag', 'bill', 'fig'],
    1: ['paper'],
    2: ['dress'],
    3: ['book', 'drug'],
    4: ['bread', 'medicine', 'shirt'],
    5: [],
    6: ['picture'],
}

# Define the moves
moves = [
    (0, 6, 'bill'),         # Move the bill from Box 0 to Box 6
    (0, 6, 'fig'),          # Move the fig from Box 0 to Box 6
    (3, None, 'book'),      # Remove the book from Box 3
    (3, None, 'drug'),      # Remove the drug from Box 3
    (2, 5, 'dress'),        # Move the dress from Box 2 to Box 5
    (0, 3, 'bag'),          # Move the bag from Box 0 to Box 3
    (None, 1, 'cheese'),    # Put the cheese into Box 1
    (None, 1, 'train'),     # Put the train into Box 1
    (1, None, 'cheese'),    # Remove the cheese from Box 1
    (1, None, 'train'),     # Remove the train from Box 1
    (6, 5, 'bill'),         # Move the bill from Box 6 to Box 5
    (6, 5, 'fig'),          # Move the fig from Box 6 to Box 5
    (5, None, 'bill'),      # Remove the bill from Box 5
    (6, None, 'picture'),   # Remove the picture from Box 6
    (None, 1, 'guitar'),    # Put the guitar into Box 1
    (3, None, 'bag'),       # Remove the bag from Box 3
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