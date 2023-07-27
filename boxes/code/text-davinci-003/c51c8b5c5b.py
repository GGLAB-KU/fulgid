# Initialize the boxes
boxes = {
    0: ['phone', 'ticket'],
    1: ['document', 'pipe', 'shirt'],
    2: ['boot', 'brain', 'guitar'],
    3: ['knife', 'stone'],
    4: ['card', 'cross', 'fig'],
    5: ['watch'],
    6: ['drug'],
}

# Define the moves
moves = [
    (6, None, 'drug'),       # Remove the drug from Box 6
    (2, None, 'brain'),      # Remove the brain from Box 2
    (2, None, 'guitar'),     # Remove the guitar from Box 2
    (1, 0, 'document'),      # Move the document from Box 1 to Box 0
    (0, 2, 'phone'),         # Move the phone from Box 0 to Box 2
    (5, None, 'watch'),      # Remove the watch from Box 5
    (4, 6, 'card'),          # Move the card from Box 4 to Box 6
    (4, 6, 'cross'),         # Move the cross from Box 4 to Box 6
    (4, 6, 'fig'),           # Move the fig from Box 4 to Box 6
    (None, 1, 'jacket'),     # Put the jacket into Box 1
    (None, 6, 'crown'),      # Put the crown into Box 6
    (0, 4, 'document'),      # Move the document from Box 0 to Box 4
    (6, None, 'card'),       # Remove the card from Box 6
    (6, None, 'cross'),      # Remove the cross from Box 6
    (6, None, 'crown'),      # Remove the crown from Box 6
    (4, None, 'document'),   # Remove the document from Box 4
    (4, None, 'fig')         # Remove the fig from Box 4
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