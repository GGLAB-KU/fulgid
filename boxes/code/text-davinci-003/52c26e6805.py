# Initialize the boxes
boxes = {
    0: ['beer', 'computer', 'key'],
    1: ['bone', 'note', 'ticket'],
    2: [],
    3: ['hat'],
    4: ['television', 'wire'],
    5: [],
    6: ['knife', 'radio', 'tape'],
}

# Define the moves
moves = [
    (0, None, 'computer'),   # Remove the computer from Box 0
    (0, None, 'key'),        # Remove the key from Box 0
    (3, None, 'hat'),        # Remove the hat from Box 3
    (None, 5, 'drug'),       # Put the drug into Box 5
    (None, 5, 'seed'),       # Put the seed into Box 5
    (4, None, 'television'),  # Remove the television from Box 4
    (4, None, 'wire'),       # Remove the wire from Box 4
    (6, 3, 'knife'),         # Move the knife from Box 6 to Box 3
    (6, 3, 'radio'),         # Move the radio from Box 6 to Box 3
    (6, 5, 'tape'),          # Move the tape from Box 6 to Box 5
    (3, None, 'knife'),      # Remove the knife from Box 3
    (3, None, 'radio'),      # Remove the radio from Box 3
    (5, 0, 'seed'),          # Move the seed from Box 5 to Box 0
    (0, 4, 'beer'),          # Move the beer from Box 0 to Box 4
    (0, 4, 'seed'),          # Move the seed from Box 0 to Box 4
    (4, None, 'beer'),       # Remove the beer from Box 4
    (5, None, 'drug'),       # Remove the drug from Box 5
    (5, None, 'tape'),       # Remove the tape from Box 5
    (4, 0, 'seed'),          # Move the seed from Box 4 to Box 0
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